
import pandas as pd
from pathlib import Path

def load_universe():
    path = Path(__file__).resolve().parents[2] / "data/tickers.csv"
    df = pd.read_csv(path)
    return df["ticker"].tolist()
