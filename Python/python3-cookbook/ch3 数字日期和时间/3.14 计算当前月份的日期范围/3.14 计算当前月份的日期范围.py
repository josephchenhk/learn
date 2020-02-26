# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 4:18 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.14 计算当前月份的日期范围.py
# @Software: PyCharm

"""
3.14 计算当前月份的日期范围

"""

from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    # Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for year, month
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month-1) #  原书没有减1，有bug
    return (start_date, end_date)

# Another way to achieve the same function
def get_month_range2(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    # 一个月至少28天
    end_date1 = start_date + timedelta(days=27)
    end_date2 = start_date + timedelta(days=28)
    end_date3 = start_date + timedelta(days=39)
    end_date4 = start_date + timedelta(days=30)
    end_date5 = start_date + timedelta(days=31)
    if end_date2.month!=start_date.month:
        return (start_date, end_date1)
    elif end_date3.month!=start_date.month:
        return (start_date, end_date2)
    elif end_date4.month!=start_date.month:
        return (start_date, end_date3)
    elif end_date5.month!=start_date.month:
        return (start_date, end_date4)

# 生成器，获得该月份所有日期
def get_month_days(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    yield start_date
    next_date = start_date + timedelta(days=1)
    while(next_date.month==start_date.month):
        yield next_date
        next_date += timedelta(days=1)

print(get_month_range())
print(get_month_range2())

print("\n----------- days -------------\n")
print(list(get_month_days()))

