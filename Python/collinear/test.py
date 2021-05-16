# -*- coding: utf-8 -*-
# @Time    : 14/5/2021 11:30 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test.py
# @Software: PyCharm
import random
from typing import Dict, List

import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor



def find_correlation_with_threshold(data:pd.DataFrame, threshold:float)->Dict[str, float]:
    corr = data.corr(method="pearson")
    corr_pair = dict()
    for i, row_tag in enumerate(data.columns[:-1]):
        for j in range(i+1, len(data.columns)):
            col_tag = data.columns[j]
            if abs(corr.loc[row_tag, col_tag])>threshold:
                corr_pair[f"{row_tag}|{col_tag}"] = corr.loc[row_tag, col_tag]
    return corr_pair

def find_possible_collinear_columns(corr_pair:Dict[str, float])->List[List[str]]:
    if len(corr_pair)==0:
        return [[]]
    if len(corr_pair)==1:
        left, right = list(corr_pair.keys())[0].split("|")
        return [[left], [right]]
    columns = [k.split("|") for k in corr_pair.keys()]
    columns = [c for col in columns for c in col]
    columns = list(set(columns))
    occurrance = {tag: sum(1 for pair in corr_pair if tag in pair) for tag in columns}
    sorted_occurrance = {k:v for k, v in sorted(occurrance.items(), key=lambda item: item[1], reverse=True)}
    col = list(sorted_occurrance.keys())[0]
    cnt = sorted_occurrance[col]

    results = []
    for col,col_cnt in sorted_occurrance.items():
        if col_cnt==cnt:
            sub_corr_pair = {k:v for k,v in corr_pair.items() if col not in k}
            res = find_possible_collinear_columns(corr_pair=sub_corr_pair)
            for r in res:
                r.insert(0, col)
            results.extend(res)

    nondup_results = []
    for res in results:
        if set(res) not in nondup_results:
            nondup_results.append(set(res))

    nondup_results = [list(r) for r in nondup_results]
    return nondup_results


def find_collinear_columns(data:pd.DataFrame, corr_threshold:float, vif_threshold:float) -> List[str]:
    corr_pair = find_correlation_with_threshold(data, corr_threshold)
    possible_collinear_cols = find_possible_collinear_columns(corr_pair)

    collinear_columns = None
    collinear_columns_avg_vif = float("inf")
    for collinear_cols in possible_collinear_cols:
        vif = [variance_inflation_factor(data.values, data.columns.get_loc(i)) for i in collinear_cols]
        print(collinear_cols, vif)
        if (np.array(vif)>vif_threshold).all():
            if collinear_columns is None or sum(vif)>collinear_columns_avg_vif:
                collinear_columns = collinear_cols
                collinear_columns_avg_vif = sum(vif)
    return collinear_columns





if __name__=="__main__":
    x1 = list(range(200))
    x2 = [x + random.randint(0, 100) / 100 for x in x1]
    x3 = [200 - x - random.randint(0, 100) / 100 for x in x1]
    x4 = [random.randint(0, 200) for _ in x1]
    X = pd.DataFrame(dict(
        x1=x1,
        x2=x2,
        x3=x3,
        x4=x4
    ))

    res = find_collinear_columns(data=X, corr_threshold=0.7, vif_threshold=5)
    # 当VIF<10,说明不存在多重共线性；当10<=VIF<100,存在较强的多重共线性，当VIF>=100,存在严重多重共线性
    # vif = [variance_inflation_factor(X.values, X.columns.get_loc(i)) for i in X.columns]
    print()