# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 2:53 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.13 计算最后一个周五的日期.py
# @Software: PyCharm

"""
3.13 计算最后一个周五的日期

"""

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(datetime.today())                # For reference
print(get_previous_byday('Monday'))    # Previous week, not today
print(get_previous_byday('Wednesday')) # Previous week, not today
print(get_previous_byday('Friday'))    # Previous week, not today

"""
如果你要像这样执行大量的日期计算的话，你最好安装第三方包 python-dateutil 来代替。 比如，下面是是使用 dateutil 模块中的 relativedelta()
函数执行同样的计算：
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO,TU,WE,TH,FR,SA,SU
d = datetime.now()
print(d)

# Next Friday
print(d + relativedelta(weekday=FR))

# Last Friday
print(d + relativedelta(weekday=FR(-1)))
