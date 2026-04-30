
def compute_value(info):
    return {
        "pe": info.get("trailingPE"),
        "pb": info.get("priceToBook")
    }