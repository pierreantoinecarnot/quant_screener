
import yfinance as yf

def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)

    hist = stock.history(period="1y")
    info = stock.info

    return hist, info