# -*- coding: utf-8 -*-
# @Time    : 2/4/2021 10:40 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: data_processing.py
# @Software: PyCharm

################################
# 处理dataframe的'Unnamed: 0'列
################################
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


################################
# 将csv文件分别移动到相应的文件夹
################################
import shutil
import os


DATA_PATH = "/Users/joseph/Dropbox/code/stat-arb/data"

k1m_files = [f for f in os.listdir(f"{DATA_PATH}/k_line/K_1M") if ".csv" in f]
codes = list(set(f.split("-")[0] for f in k1m_files))

for code in codes:
    print(f"handling {code}")
    if not os.path.exists(f"{DATA_PATH}/k_line/K_1M/{code}"):
        os.mkdir(f"{DATA_PATH}/k_line/K_1M/{code}")
    code_files = [f for f in k1m_files if code in f]
    for code_file in code_files:
        date = code_file[9:]
        shutil.move(f"{DATA_PATH}/k_line/K_1M/{code_file}", f"{DATA_PATH}/k_line/K_1M/{code}/{date}")
print("Done.")
