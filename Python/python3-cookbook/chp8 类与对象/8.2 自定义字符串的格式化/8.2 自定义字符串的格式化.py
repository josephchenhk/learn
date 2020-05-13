# -*- coding: utf-8 -*-
# @Time    : 7/18/2019 3:46 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.2 自定义字符串的格式化.py
# @Software: PyCharm

"""
8.2 自定义字符串的格式化

通过 format() 函数和字符串方法使得一个对象能支持自定义的格式化
"""

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2019, 6, 20)
print("The date is {:ymd}".format(d))
print("The date is {:mdy}".format(d))
print("The date is {:dmy}".format(d))

print(format(d, "mdy"))