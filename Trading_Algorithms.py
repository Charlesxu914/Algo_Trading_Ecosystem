import numpy as np
import pandas as pd


def random_data(financial_data):
    name = "Random Trading Strategy"
    signals = pd.DataFrame(index=financial_data.index)
    data = np.random.randint(0, 2, size=financial_data.shape[0])
    # data = np.ones(financial_data.shape[0])
    # data[0] = 0
    data[financial_data.shape[0] - 1] = 0
    signals['signal'] = data  # position
    # 00000011111111110000000000 # position
    # 000000100000000-1000000000 # orders
    signals['orders'] = signals['signal'].diff()  # orders
    return signals, name


def moving_average(financial_data, short_window, long_window):
    name = "Moving Average Strategy"
    signals = pd.DataFrame(index=financial_data.index)
    signals['signal'] = 0.0
    signals['short_avg'] = financial_data['Close'].rolling(window=short_window, min_periods=1,
                                                           center=False).mean()
    signals['long_avg'] = financial_data['Close'].rolling(window=long_window, min_periods=1,
                                                          center=False).mean()
    signals['signal'][short_window:] = np.where(signals['short_avg'][short_window:]
                                                > signals['long_avg'][short_window:], 1, 0)
    signals['signal'][financial_data.shape[0] - 1] = 0
    signals['orders'] = signals['signal'].diff()
    # pd.set_option("display.max_rows", 9999)
    # print(signals)
    return signals, name

def OBV_indicator(financial_data):
    name = "OBV_indicator Strategy"
    OBV_data = pd.DataFrame(index=financial_data.index)
    OBV_data['OBV'] = np.where(financial_data['Close'] > financial_data['Close'].shift(1), 1, -1)
    OBV_data['OBV'][0] = 0
    OBV_data['OBV'] = (OBV_data['OBV'] * financial_data['Volume']).cumsum()
    OBV_data['OBV ema'] = OBV_data['OBV'].ewm(com=5).mean()
    signals = pd.DataFrame({'signal':np.where(OBV_data['OBV']>OBV_data['OBV ema'], 1, 0)},index=OBV_data.index)
    signals['signal'][financial_data.shape[0] - 1] = 0
    signals['orders'] = signals['signal'].diff()
    return signals, name


def MACD(financial_data, short_window, long_window):
    name = "MACD Indicator Strategy"
    MACD_data = pd.DataFrame(index=financial_data.index)
    MACD_data["st_ema"] = financial_data['Close'].ewm(span = short_window).mean()
    MACD_data["lt_ema"] = financial_data['Adj Close'].ewm(span = long_window).mean()
    MACD_data["MACD"] = MACD_data["st_ema"] - MACD_data["lt_ema"]
    MACD_data["MACD_signal"] = MACD_data["MACD"].ewm(span = 9).mean()
    signals = pd.DataFrame({'signal':np.where(MACD_data['MACD']>MACD_data['MACD_signal'], 1, 0)},index=MACD_data.index)
    signals['signal'][1] = 0
    signals['signal'][financial_data.shape[0]-1] = 0
    signals['orders'] = signals['signal'].diff() 
    return signals, name


def RSI_indicator(financial_data, RSI_period):
    name = "RSI Indicator Strategy"
    RSI_data = pd.DataFrame(index=financial_data.index)
    RSI_data['diff'] = financial_data['Close'].diff()
    RSI_data['gain'] = RSI_data['diff']
    RSI_data['gain'][1:] = np.where(RSI_data['diff'][1:] > 0, RSI_data['diff'][1:], 0)
    RSI_data['loss'] = RSI_data['diff']
    RSI_data['loss'][1:] = np.where(RSI_data['diff'][1:] < 0, -RSI_data['diff'][1:], 0)
    RSI_data['avg_gain'] = RSI_data["gain"].rolling(RSI_period).mean()
    RSI_data['avg_gain'][RSI_period+1:] = RSI_data["gain"][RSI_period+1:]
    RSI_data['avg_gain'] = RSI_data["avg_gain"].ewm(com=RSI_period-1, adjust = False).mean()
    RSI_data['avg_loss'] = RSI_data["loss"].rolling(RSI_period).mean()
    RSI_data['avg_loss'][RSI_period+1:] = RSI_data["loss"][RSI_period+1:]
    RSI_data['avg_loss'] = RSI_data["avg_loss"].ewm(com=RSI_period-1, adjust = False).mean()
    RSI_data['RSI'] = 100 - 100/(1+RSI_data['avg_gain']/RSI_data['avg_loss'])
    signal = np.where(RSI_data['RSI'] < 30, 1, 
         (np.where(RSI_data['RSI'] > 70, 0, np.nan)))
    position = signal
    for i in range(1, len(position)):
        if np.isnan(position[i]):
            if np.isnan(position[i-1]):
                position[i] = 0
            else:
                position[i] = position[i-1]
    position[0] = 0
    position[-1] = 0
    signals = pd.DataFrame(index=financial_data.index)
    signals['signal'] = position
    signals['orders'] = signals['signal'].diff()
    return signals, name




