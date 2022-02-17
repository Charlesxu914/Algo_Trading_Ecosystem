from Load_Data import *
from Trading_Algorithms import *
from Plot import *
from Build_Portfolio import *
import pandas as pd


if __name__ == "__main__":
    ticker = 'GOOG'
    initial_capital = 10000
    goog_data = load_financial_data(ticker = 'GOOG',
                                    start_date='2001-01-01',
                                    end_date='2018-01-01',
                                    output_file='data.pkl')
    # trading strategy
    ts, name = random_data(goog_data, 20, 100)
    signals = ts
    plot_operation(goog_data, ts, name)
    portfolio = build_portfolio(ticker, goog_data, ts, initial_capital, signals)
    pd.set_option("display.max_rows", 9999)
    pd.set_option("display.max_columns", 4)
    print(portfolio)
    plot_pnl(portfolio, name)




