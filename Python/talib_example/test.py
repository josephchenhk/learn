# -*- coding: utf-8 -*-
# @Time    : 4/5/2021 3:13 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm
import pandas as pd
import talib as ta

DATA_PATH = "/Users/joseph/Dropbox/code/stat-arb/data/k_line/K_1M"

def get_data():
    df = pd.read_csv(f"{DATA_PATH}/HK.00981/2021-04-23.csv")
    return df

if __name__=="__main__":
    ta_functions = ta.get_functions()
    print(f"Number of functions in TALIB: {len(ta_functions)}")
    ta_funciton_groups = ta.get_function_groups()
    print(f"TALIB function groups:")
    for group_name, functions in ta_funciton_groups.items():
        print(f"{len(functions)} functions in {group_name}: {functions}")

    data = get_data()
    # 3 functions in Volatility Indicators: ['ATR', 'NATR', 'TRANGE']
    # (1). Average True Range (Volatility Indicator)
    atr = ta.ATR(high=data["high"], low=data["low"], close=data["close"], timeperiod=14)
    print()