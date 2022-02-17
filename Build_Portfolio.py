import pandas as pd


def build_portfolio(ticker, data, trading_strategy, initial, signals):
    initial_capital = float(initial)
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    positions[ticker] = 10 * trading_strategy['signal']
    portfolio = positions.multiply(data['Adj Close'], axis=0)
    portfolio['holdings'] = (positions.multiply(data['Adj Close'], axis=0)).sum(axis=1)
    pos_diff = positions.diff()
    portfolio['cash'] = initial_capital - (pos_diff.multiply(data['Adj Close'], axis=0)).sum(axis=1).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    # portfolio['daily_returns'] = portfolio['total'].pct_change()
    portfolio['total_returns'] = ((portfolio['total'] - initial)/initial * 100).round(2).astype(str) + '%'
    return portfolio
    # print(portfolio)
