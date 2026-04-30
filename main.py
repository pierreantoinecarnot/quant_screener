
from src.data.universe import load_universe
from src.data.loader import fetch_stock_data
from src.factors.momentum import compute_momentum
from src.factors.value import compute_value
from src.factors.quality import compute_quality
from src.scoring.scorer import score_stock

import pandas as pd

tickers = load_universe()

results = []

for t in tickers:
    try:
        hist, info = fetch_stock_data(t)

        if hist.empty:
            continue

        perf_6m, perf_12m = compute_momentum(hist["Close"])
        value = compute_value(info)
        quality = compute_quality(info)

        score = score_stock(value, quality, perf_6m, perf_12m)

        results.append({
            "ticker": t,
            "score": score
        })

    except:
        continue

df = pd.DataFrame(results).sort_values("score", ascending=False)

print(df.head(10))