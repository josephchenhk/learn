# -*- coding: utf-8 -*-
# @Time    : 20/5/2021 9:42 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test.py
# @Software: PyCharm

import pandas as pd

def bet_type(type:str):
    if "进球" in type:
        type = type.replace("进球数", "进球")
        if "进球大" in type and "进球大于" not in type:
            type = type.replace("进球大", "进球大于")
        if "进球小" in type and "进球小于" not in type:
            type = type.replace("进球小", "进球小于")
        return type
    elif "角球" in type:
        return type
    elif "+" in type:
        return "让球+" + type.split("+")[-1]
    elif "-" in type:
        return "让球-" + type.split("-")[-1]
    else:
        return "未知"

df = None
for month in range(1, 5+1):
    sheet_name = f"2021.{month:02d}"
    print(sheet_name)

    df1 = pd.read_excel("2021年微博比赛.xlsx", sheet_name=sheet_name, skiprows=2)
    df1 = df1[df1['红黑'].notna()]
    if df is None:
        df = df1
    else:
        df = pd.concat([df, df1])

df["玩法分类"] = df["玩法"].apply(bet_type)

path = "2021年微博比赛结果分析.xlsx"
writer = pd.ExcelWriter(path, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name="汇总")

res = df.groupby(['联赛']).sum()
res["盈利比例"] = res["盈利"] / res["投入"]
res.to_excel(writer, sheet_name="联赛")

res = df.groupby(['玩法分类']).sum()
res["盈利比例"] = res["盈利"] / res["投入"]
res.to_excel(writer, sheet_name="玩法分类")

writer.save()
writer.close()
print("Well done!")