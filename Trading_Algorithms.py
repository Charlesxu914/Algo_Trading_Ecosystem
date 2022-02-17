import numpy as np
import pandas as pd


def random_data(financial_data, short_window, long_window):
    signals = pd.DataFrame(index=financial_data.index)
    # data = np.random.randint(0, 2, size=financial_data.shape[0])
    data = np.ones(financial_data.shape[0])
    data[0] = 0
    data[financial_data.shape[0] - 1] = 0

    signals['signal'] = data  # position
    # 00000011111111110000000000 # position
    # 000000100000000-1000000000 # orders
    signals['orders'] = signals['signal'].diff()  # orders
    return signals
