import datetime
import pandas as pd
import os

DATA_PATH = "data/student_logs.csv"

def append_daily_record(text, screen_time, typing_wpm, burnout_score):
    row = {
        "date": datetime.date.today().isoformat(),
        "text": text,
        "screen_time": float(screen_time),
        "typing_wpm": float(typing_wpm),
        "burnout_score": float(burnout_score)
    }
    df = pd.DataFrame([row])
    header = not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0
    df.to_csv(DATA_PATH, mode='a', header=header, index=False)
    return row