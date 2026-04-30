
from config import MAX_PE, MAX_PB, MIN_ROE, MIN_VOLUME

def score_stock(value, quality, perf_6m, perf_12m):
    score = 0

    pe = value["pe"]
    pb = value["pb"]

    if pe and pe < MAX_PE:
        score += 20
    if pb and pb < MAX_PB:
        score += 20

    if perf_6m > 0:
        score += 20
    if perf_12m > 0:
        score += 20

    if quality["roe"] > MIN_ROE:
        score += 10
    if quality["debt"] < 1:
        score += 10

    if quality["volume"] < MIN_VOLUME:
        score -= 50  # pénalité liquidité

    return score