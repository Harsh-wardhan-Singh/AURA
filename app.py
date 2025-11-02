# app.py
import streamlit as st
from src.sentiment_analysis import get_sentiment_score
from src.burnout_model import compute_burnout
from src.comfort_mode import pick_message
from src.collect_data import append_daily_record
import pandas as pd
import os

st.set_page_config(page_title="AURA - BurnoutGuard", layout="centered")

st.title("AURA — Student Wellbeing Prototype")
st.write("Type how your day was, give simple metrics, and we’ll assess your wellbeing.")

text = st.text_area("How are you feeling today? (one line is fine)", height=120)
screen_time = st.number_input("Hours on study/online today (approx)", min_value=0.0, max_value=24.0, value=3.0, step=0.5)
typing_wpm = st.number_input("Approx typing speed (wpm) today", min_value=5.0, max_value=150.0, value=40.0, step=1.0)

if st.button("Analyze my wellbeing"):
    # sentiment
    sentiment = get_sentiment_score(text)
    # burnout score
    burnout = compute_burnout(sentiment, screen_time, typing_wpm)
    st.subheader(f"Burnout risk: {burnout:.2f} / 1.0")
    # comfort or normal
    message = pick_message(burnout)
    if burnout >= 0.75:
        st.error("High risk detected — take a breath. Below are suggestions.")
    elif burnout >= 0.45:
        st.warning("Moderate risk — try a micro-break.")
    else:
        st.success("Low risk — keep going!")
    st.write(message)

    # save data
    row = append_daily_record(text, screen_time, typing_wpm, burnout)
    st.info("Saved today's entry (for trend analysis).")

# teacher monthly chart
if st.button("Show saved trend (teacher view)"):
    try:
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), "data", "student_logs.csv"), parse_dates=["date"])
        df = df.sort_values("date")
        st.line_chart(df.set_index("date")["burnout_score"])
        st.dataframe(df.tail(10))
    except Exception as e:
        st.error("No saved data yet. Fill the form and click Analyze first.")