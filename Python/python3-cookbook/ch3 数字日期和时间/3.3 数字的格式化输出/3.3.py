# -*- coding: utf-8 -*-
# @Time    : 13/2/2020 11:17 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 3.3.py
# @Software: PyCharm

"""
3.3 数字的格式化输出


"""
x = 1234.56789
print(format(x, '>10.1f'))  # 靠右 '    1234.6'
print(format(x, '<10.1f'))  # 靠左 '1234.6    '
print(format(x, '^10.1f'))  # 靠中 '  1234.6  '

print(format(x, '0.2e')) # 科学计数 '1.23e+03'

"""
同时指定宽度和精度的一般形式是 '[<>^]?width[,]?(.digits)?' ， 其中 width 和 digits 为整数，？代表可选部分。 同样的格式也被用在字符串的 format() 
"""
print('The value is {:,.2f}'.format(x))  # The value is 1,234.57
print('The value is ' + format(x, ',.2f'))  # The value is 1,234.57
