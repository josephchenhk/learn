# -*- coding: utf-8 -*-
# @Time    : 20/5/2021 9:42 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test.py
# @Software: PyCharm

import pandas as pd

def bet_type(type_:str):
    if type(type_) != str:
        print(type_)
        return "未知"
    if "进球" in type_:
        type_ = type_.replace("进球数", "进球")
        if "进球大" in type_ and "进球大于" not in type_:
            type_ = type_.replace("进球大", "进球大于")
        if "进球小" in type_ and "进球小于" not in type_:
            type_ = type_.replace("进球小", "进球小于")
        return type_
    elif "角球" in type_:
        return type_
    elif "+" in type_:
        return "让球+" + type_.split("+")[-1]
    elif "-" in type_:
        return "让球-" + type_.split("-")[-1]
    else:
        return "未知"

def drop_unnamed_cols(df: pd.DataFrame) ->pd.DataFrame:
    unnamed_cols = []
    for col in df.columns:
        if "Unnamed" in col:
            unnamed_cols.append(col)
    if unnamed_cols:
        return df.drop(columns=unnamed_cols)
    return df

df = None
year = 2021
for month in range(1, 12+1):
    sheet_name = f"{year}.{month:02d}"
    print(sheet_name)

    try:
        df1 = pd.read_excel(f"{year}年比赛统计.xlsx", sheet_name=sheet_name, skiprows=2)
    except ValueError as e:
        print(e)
        continue

    df1 = df1[df1['红黑'].notna()]
    if df is None:
        df = df1
    else:
        df = pd.concat([df, df1])

df["玩法分类"] = df["玩法"].apply(bet_type)
df["投入"] = df["投入"].astype(float)

path = f"{year}年微博比赛结果分析.xlsx"
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name="汇总")

res = df.groupby(['联赛']).sum()
res["盈利比例"] = res["盈利"] / res["投入"]
res = drop_unnamed_cols(res)
res.to_excel(writer, sheet_name="联赛")

res = df.groupby(['玩法分类']).sum()
res["盈利比例"] = res["盈利"] / res["投入"]
res = drop_unnamed_cols(res)
res.to_excel(writer, sheet_name="玩法分类")

def over_under(x:str):
    if "进球大于" in x:
        return "进球大"
    elif "进球小于" in x:
        return "进球小"
    elif "角球大于" in x:
        return "角球大"
    elif "角球小于" in x:
        return "角球小"
    else:
        return None

df["大小球"] = df["玩法分类"].apply(lambda x: over_under(x))
res = df.dropna(subset=["大小球"]).groupby(["大小球"]).sum()
if not res.empty:
    res["盈利比例"] = res["盈利"] / res["投入"]
    res_cnt = df.dropna(subset=["大小球"]).groupby(["大小球"]).count()["玩法分类"]
    res_cnt.name = "下注次数"
    res = res.join(res_cnt)
    res = drop_unnamed_cols(res)
    res.to_excel(writer, sheet_name="大小球")

def asian_handicap(x:str):
    if "-" in x:
        return "上盘"
    elif "+" in x:
        return "下盘"
    else:
        return None

df["让球"] = df["玩法分类"].apply(lambda x: asian_handicap(x))
res = df.dropna(subset=["让球"]).groupby(["让球"]).sum()
if not res.empty:
    res["盈利比例"] = res["盈利"] / res["投入"]
    res_cnt = df.dropna(subset=["让球"]).groupby(["让球"]).count()["玩法分类"]
    res_cnt.name = "下注次数"
    res = res.join(res_cnt)
    res = drop_unnamed_cols(res)
    res.to_excel(writer, sheet_name="让球")

writer.save()
print("Well done!")