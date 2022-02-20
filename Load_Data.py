import numpy as np
import pandas as pd
import pandas_datareader
from pandas_datareader import data


def load_financial_data(ticker, start_date, end_date, output_file):
    try:
        df = pd.read_pickle(output_file)
        print('File data found...reading data')
    except FileNotFoundError:
        print('File not found...downloading the data')
        df = data.DataReader(ticker, 'yahoo', start_date, end_date)
        df.to_pickle(output_file)
    return df