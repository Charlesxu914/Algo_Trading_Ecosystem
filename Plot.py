import matplotlib.pyplot as plt


def plot_operation(data, trading_strategy, strategy_name):
    fig = plt.figure(figsize=(12, 9))
    ax1 = fig.add_subplot(111, ylabel='Google price in $')
    data["Adj Close"].plot(ax=ax1, color='g', lw=.5)
    ax1.plot(trading_strategy.loc[trading_strategy.orders == 1.0].index,
             data["Adj Close"][trading_strategy.orders == 1.0],
             '^', markersize=7, color='k')
    ax1.plot(trading_strategy.loc[trading_strategy.orders == -1.0].index,
             data["Adj Close"][trading_strategy.orders == -1.0],
             'v', markersize=7, color='k')
    # trading_strategy['short_avg'].plot(ax=ax1, color = 'r', lw = 2.)
    # trading_strategy['long_avg'].plot(ax=ax1, color='b', lw=2.)
    plt.legend(["Price", "Buy", "Sell"])
    plt.title(strategy_name)
    plt.show()


def plot_pnl(portfolio, strategy_name):
    # portfolio['holdings'].plot(color='g', lw=.5)
    plt.figure(figsize=(12, 9))
    # portfolio['cash'].plot(color='r', lw=.5)
    portfolio['total'].plot(color='g', lw=.5)
    plt.title(strategy_name + ' P&L')
    plt.show()
