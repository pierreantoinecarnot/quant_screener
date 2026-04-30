
import pandas as pd

def load_universe(path="data/tickers.csv"):
    df = pd.read_csv(path)
    return df["ticker"].tolist()