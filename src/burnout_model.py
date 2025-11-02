# src/burnout_model.py
import numpy as np

# Use a simple interpretable formula for MVP:
# burnout_score in [0,1] where higher means more likely burnout
def compute_burnout(sentiment_score, screen_time_hours, typing_wpm, baseline_typing=40):
    # Normalize features
    neg_sent = max(0.0, -sentiment_score)  # 0..1
    screen_factor = min(screen_time_hours / 10.0, 1.0)  # 0..1 (10h -> 1)
    typing_drop = max(0.0, (baseline_typing - typing_wpm) / (baseline_typing + 1))  # 0..1
    # weighted sum (tune later)
    score = 0.45 * neg_sent + 0.35 * screen_factor + 0.20 * typing_drop
    score = float(np.clip(score, 0.0, 1.0))
    return score
