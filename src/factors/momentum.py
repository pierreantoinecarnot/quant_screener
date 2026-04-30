
def compute_momentum(prices):
    if len(prices) < 200:
        return 0, 0

    perf_6m = prices.iloc[-1] / prices.iloc[-126] - 1
    perf_12m = prices.iloc[-1] / prices.iloc[0] - 1

    return perf_6m, perf_12m