
import yfinance as yf

def backtest_portfolio(tickers):
    returns = []

    for t in tickers:
        try:
            hist = yf.Ticker(t).history(period="1y")

            if len(hist) < 200:
                continue

            ret = hist["Close"].iloc[-1] / hist["Close"].iloc[0] - 1
            returns.append(ret)

        except:
            continue

    if not returns:
        return 0

    return sum(returns) / len(returns)