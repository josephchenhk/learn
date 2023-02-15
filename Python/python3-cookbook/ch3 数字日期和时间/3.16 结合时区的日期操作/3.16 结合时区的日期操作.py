# -*- coding: utf-8 -*-
# @Time    : 26/2/2020 4:54 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.16 结合时区的日期操作.py
# @Software: PyCharm

"""
3.16 结合时区的日期操作

对几乎所有涉及到时区的问题，你都应该使用 pytz 模块。这个包提供了Olson时区数据库， 它是时区信息的事实上的标准，在很多语言和操作系统里面都可以找到
"""

from datetime import datetime, timedelta
import pytz
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)       # 2012-12-21 09:30:00

# Localize the date for Chicago
central = pytz.timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)   # 2012-12-21 09:30:00-06:00

# 一旦日期被本地化了， 它就可以转换为其他时区的时间了。例如：Convert to Bangalore time
bang_d = loc_d.astimezone(pytz.timezone('Asia/Kolkata'))
print(bang_d)  # 2012-12-21 21:00:00+05:30

"""
如果你打算在本地化日期上执行计算，你需要特别注意夏令时转换和其他细节。 比如，在2013年，美国标准夏令时时间开始于本地时间3月13日凌晨2:00(在那时，
时间向前跳过一小时)。 如果你正在执行本地计算，你会得到一个错误。比如：
"""
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)  # 2013-03-10 01:45:00-06:00
later = loc_d + timedelta(minutes=30)
print(later)  # 2013-03-10 02:15:00-06:00 (这是错误的！因为夏令时跳过了2时！)

# 正确的做法是：使用时区对象 normalize()方法
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)  # 2013-03-10 03:15:00-05:00

"""
为了不让你被这些东东弄的晕头转向，处理本地化日期的通常的策略先将所有日期转换为UTC时间， 并用它来执行所有的中间存储和操作。一旦转换为UTC，你就不用
去担心跟夏令时相关的问题了。 因此，你可以跟之前一样放心的执行常见的日期计算。 当你想将输出变为本地时间的时候，使用合适的时区去转换下就行了。
"""
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)  # 2013-03-10 07:45:00+00:00
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central)) # 2013-03-10 03:15:00-05:00

"""
当涉及到时区操作的时候，有个问题就是我们如何得到时区的名称。 比如，在这个例子中，我们如何知道“Asia/Kolkata”就是印度对应的时区名呢？ 为了查找，
可以使用ISO 3166国家代码作为关键字去查阅字典 pytz.country_timezones 。比如：
"""
print(pytz.country_timezones['IN']) # ['Asia/Kolkata']
print(pytz.country_timezones['CN']) # ['Asia/Shanghai', 'Asia/Urumqi']
print(pytz.country_timezones['HK']) # ['Asia/Hong_Kong']
print(pytz.country_timezones['US']) # ['America/New_York', 'America/Detroit', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Indiana/Indianapolis', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Vevay', 'America/Chicago', 'America/Indiana/Tell_City', 'America/Indiana/Knox', 'America/Menominee', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/North_Dakota/Beulah', 'America/Denver', 'America/Boise', 'America/Phoenix', 'America/Los_Angeles', 'America/Anchorage', 'America/Juneau', 'America/Sitka', 'America/Metlakatla', 'America/Yakutat', 'America/Nome', 'America/Adak', 'Pacific/Honolulu']
