
def compute_quality(info):
    return {
        "roe": info.get("returnOnEquity", 0),
        "debt": info.get("debtToEquity", 999),
        "volume": info.get("volume", 0)
    }