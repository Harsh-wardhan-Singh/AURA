# src/comfort_mode.py
import json
import random

def load_messages(path="data/motivation.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["comfort"]

def pick_message(burnout_score):
    messages = load_messages()
    if burnout_score < 0.45:
        return "You seem okay today — keep going! 😊"
    if burnout_score < 0.75:
        return random.choice(messages)
    # high burnout -> stronger encouragement
    return "I see things are difficult. It's okay to ask for help — talk to a friend or counselor. " + random.choice(messages)