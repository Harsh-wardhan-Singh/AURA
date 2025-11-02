# src/sentiment_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(text: str) -> float:
    """
    Returns compound sentiment score in range [-1, 1].
    Negative -> closer to -1, Positive -> closer to +1
    """
    if not text or text.strip() == "":
        return 0.0
    score = _analyzer.polarity_scores(text)["compound"]
    return score