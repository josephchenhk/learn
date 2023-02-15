# -*- coding: utf-8 -*-
# @Time    : 20/5/2021 9:42 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py
# @Software: PyCharm
from typing import Dict
import pandas as pd
from xlsxwriter.workbook import Workbook

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

def format_sheet(
        data: pd.DataFrame,
        workbook: Workbook,
        sheet_name: str,
        format: Dict[str, str]
):
    # Adding formats for header row.
    fmt_header = workbook.add_format(
        {
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#5DADE2',
            'font_color': '#FFFFFF',
            'border': 1,
        }
    )
    # Adding percentage format.
    fmt_rate = workbook.add_format(
        {
            'num_format': '%0.00',
            'bold': False
        }
    )
    # Adding currency format
    fmt_currency_cny = workbook.add_format(
        {
            'num_format': '¥#,##0.00',
            'bold': False
        }
    )
    # Adding float format
    fmt_float = workbook.add_format(
        {
            'num_format': '0.000',
            'bold': False
        }
    )
    formats = {
        'header': fmt_header,
        'rate': fmt_rate,
        'currency(¥)': fmt_currency_cny,
        'float': fmt_float
    }
    worksheet = workbook.get_worksheet_by_name(sheet_name)
    for col_name, format_name in format.items():
        if col_name == '标题':
            for col, value in enumerate(data.columns.values):
                worksheet.write(0, col+1, value, formats[format_name])
            continue
        col_idx = list(data.columns).index(col_name) + 1
        worksheet.set_column(col_idx, col_idx, 16, formats[format_name])

df = None
year = 2022
for month in range(3, 12+1):
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
df["水位"] = df["水位"].astype(float)
df["信心指数"] = df["信心指数"].astype(float)
df["期望回报"] = df["水位"] * df["信心指数"]

path = f"{year}年微博比赛结果分析.xlsx"
writer = pd.ExcelWriter(path, engine='xlsxwriter')
df.to_excel(writer, sheet_name="汇总")

res1 = df[["投入", "盈利", "联赛"]].groupby(['联赛']).sum()
res2 = df[["水位", "信心指数", "期望回报", "联赛"]].groupby(['联赛']).mean()
res3 = df[["投入", "联赛"]].groupby(['联赛']).count().rename(columns={"投入": "次数"})
res = res1.join(res2).join(res3)
res["盈利比例"] = res["盈利"] / res["投入"]
res = drop_unnamed_cols(res)
res.to_excel(writer, sheet_name="联赛")

format_sheet(
    data=res,
    workbook=writer.book,
    sheet_name='联赛',
    format={
        '标题': 'header',
        '投入': 'currency(¥)',
        '盈利': 'currency(¥)',
        '盈利比例': 'rate',
        '水位': 'float',
        '信心指数': 'float',
        '期望回报': 'float'
    }
)

res1 = df[["投入", "盈利", "玩法分类"]].groupby(['玩法分类']).sum()
res2 = df[["水位", "信心指数", "期望回报", "玩法分类"]].groupby(['玩法分类']).mean()
res3 = df[["投入", "玩法分类"]].groupby(['玩法分类']).count().rename(columns={"投入": "次数"})
res = res1.join(res2).join(res3)
res["盈利比例"] = res["盈利"] / res["投入"]
res = drop_unnamed_cols(res)
res.to_excel(writer, sheet_name="玩法分类")

format_sheet(
    data=res,
    workbook=writer.book,
    sheet_name='玩法分类',
    format={
        '标题': 'header',
        '投入': 'currency(¥)',
        '盈利': 'currency(¥)',
        '盈利比例': 'rate',
        '水位': 'float',
        '信心指数': 'float',
        '期望回报': 'float'
    }
)
print()

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
df1 = df.dropna(subset=["大小球"])
if not df1.empty:
    res1 = df1[["投入", "盈利", "大小球"]].groupby(['大小球']).sum()
    res2 = df1[["水位", "信心指数", "期望回报", "大小球"]].groupby(['大小球']).mean()
    res = res1.join(res2)
    res["盈利比例"] = res["盈利"] / res["投入"]
    res_cnt = df.dropna(subset=["大小球"]).groupby(["大小球"]).count()["玩法分类"]
    res_cnt.name = "下注次数"
    res = res.join(res_cnt)
    res = drop_unnamed_cols(res)
    res.to_excel(writer, sheet_name="大小球")

    format_sheet(
        data=res,
        workbook=writer.book,
        sheet_name='大小球',
        format={
            '标题': 'header',
            '投入': 'currency(¥)',
            '盈利': 'currency(¥)',
            '盈利比例': 'rate',
            '水位': 'float',
            '信心指数': 'float',
            '期望回报': 'float'
        }
    )

def asian_handicap(x:str):
    if "-" in x:
        return "上盘"
    elif "+" in x:
        return "下盘"
    else:
        return None

df["让球"] = df["玩法分类"].apply(lambda x: asian_handicap(x))
df1 = df.dropna(subset=["让球"])
if not res.empty:
    res1 = df1[["投入", "盈利", "让球"]].groupby(['让球']).sum()
    res2 = df1[["水位", "信心指数", "期望回报", "让球"]].groupby(['让球']).mean()
    res = res1.join(res2)
    res["盈利比例"] = res["盈利"] / res["投入"]
    res_cnt = df.dropna(subset=["让球"]).groupby(["让球"]).count()["玩法分类"]
    res_cnt.name = "下注次数"
    res = res.join(res_cnt)
    res = drop_unnamed_cols(res)
    res.to_excel(writer, sheet_name="让球")

    format_sheet(
        data=res,
        workbook=writer.book,
        sheet_name='让球',
        format={
            '标题': 'header',
            '投入': 'currency(¥)',
            '盈利': 'currency(¥)',
            '盈利比例': 'rate',
            '水位': 'float',
            '信心指数': 'float',
            '期望回报': 'float'
        }
    )

writer.save()
print("Well done!")
