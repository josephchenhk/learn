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
    timestamps = sorted([f.replace(".csv","") for f in os.listdir(f"{DATA_PATH}/{stock}")])
    dates = set(t.split(" ")[0] for t in timestamps)
    assert len(dates)==1, "data not correct"
    date = list(dates)[0]
    for idx, timestamp in enumerate(timestamps):
        df = pd.read_csv(f"{DATA_PATH}/{stock}/{timestamp}.csv")
        if idx==0:
            capital_dist = df.copy()
        else:
            capital_dist = pd.concat([capital_dist, df])
    capital_dist.to_csv(f"{DATA_PATH}/{stock}/{date}.csv")
    print(f"Save {stock}")
print("Done.")