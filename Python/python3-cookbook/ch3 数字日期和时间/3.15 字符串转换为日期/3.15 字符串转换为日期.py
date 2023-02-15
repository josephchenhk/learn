# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 4:37 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.15 字符串转换为日期.py
# @Software: PyCharm

"""
3.15 字符串转换为日期


datetime.strptime & datetime.strftime
"""

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z) # Wednesday February 26, 2020


"""
还有一点需要注意的是， strptime() 的性能要比你想象中的差很多， 因为它是使用纯Python实现，并且必须处理所有的系统本地设置。 如果你要在代码中需要
解析大量的日期并且已经知道了日期字符串的确切格式，可以自己实现一套解析方案来获取更好的性能。 比如，如果你已经知道所以日期格式是 YYYY-MM-DD ，你
可以像下面这样实现一个解析函数：

"""

from timeit import timeit

from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

print(parse_ymd("2020-02-26"))                     # 2020-02-26 00:00:00
print(datetime.strptime("2020-02-26", "%Y-%m-%d")) # 2020-02-26 00:00:00

print(timeit(lambda:parse_ymd("2020-02-26"), number=100000))                     # 0.26006787
print(timeit(lambda:datetime.strptime("2020-02-26", "%Y-%m-%d"), number=100000)) # 2.391469756

# 时间相差了快10倍！！
