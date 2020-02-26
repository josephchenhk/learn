# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 2:34 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.12 基本的日期与时间转换.py
# @Software: PyCharm

"""
3.12 基本的日期与时间转换

datetime
"""

# 一段时间：timedelta
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c) # 2 days, 10:30:00

# 时间点：datetime
from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10)) # 2012-10-03 00:00:00

"""
如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块
"""
import traceback
try:
    print(a + timedelta(months=1))
except:
    print(traceback.print_exc())    # TypeError: 'months' is an invalid keyword argument for __new__()

from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=1))  # 2012-10-23 00:00:00
