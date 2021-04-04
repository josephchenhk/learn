# -*- coding: utf-8 -*-
# @Time    : 2/4/2021 10:40 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: data_processing.py
# @Software: PyCharm

import os
import pandas as pd

DATA_PATH = "/Users/joseph/Dropbox/code/stat-arb/data/capital_distribution"

stocks = [f for f in os.listdir(DATA_PATH) if not f.startswith(".")]

for stock in stocks:
    dates = sorted([f.replace(".csv","") for f in os.listdir(f"{DATA_PATH}/{stock}") if not f.startswith(".")])

    for idx, date in enumerate(dates):
        df = pd.read_csv(f"{DATA_PATH}/{stock}/{date}.csv")
        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])
            df.to_csv(f"{DATA_PATH}/{stock}/{date}.csv", index=False)

