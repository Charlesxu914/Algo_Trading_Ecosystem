from Load_Data import *
from Trading_Algorithms import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
    goog_data = load_financial_data(start_date='2001-01-01',
                                    end_date='2018-01-01',
                                    output_file='goog_data.pkl')
    # trading strategy
    ts = random_data(goog_data, 20, 100)
    signals = ts
    fig = plt.figure(figsize=(12, 9))
    ax1 = fig.add_subplot(111, ylabel='Google price in $')
    goog_data["Adj Close"].plot(ax=ax1, color='g', lw=.5)
    ax1.plot(ts.loc[ts.orders == 1.0].index, goog_data["Adj Close"][ts.orders == 1.0],
             '^', markersize=7, color='k')
    ax1.plot(ts.loc[ts.orders == -1.0].index, goog_data["Adj Close"][ts.orders == -1.0],
             'v', markersize=7, color='k')
    plt.legend(["Price", "Short mavg", "Long mavg", "Buy", "Sell"])
    plt.title("Random Trading Strategy")
    plt.show()

    initial_capital = float(10000.0)
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    positions['GOOG'] = 10 * ts['signal']
    portfolio = positions.multiply(goog_data['Adj Close'], axis=0)
    portfolio['holdings'] = (positions.multiply(goog_data['Adj Close'], axis=0)).sum(axis=1)
    pos_diff = positions.diff()
    portfolio['cash'] = initial_capital - (pos_diff.multiply(goog_data['Adj Close'], axis=0)).sum(axis=1).cumsum()
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()
    print(portfolio)

    portfolio['holdings'].plot(color='g', lw=.5)
    plt.figure(figsize=(12, 9))
    portfolio['cash'].plot(color='r', lw=.5)
    portfolio['total'].plot(color='g', lw=.5)
    plt.title("Random Trading Strategy")
    plt.show()


