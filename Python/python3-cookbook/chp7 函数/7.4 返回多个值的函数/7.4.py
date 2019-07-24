# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 8:10 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.4.py
# @Software: PyCharm
"""
7.4 返回多个值的函数

"""

def myfun():
    return 1, 2, 3

"""
尽管myfun()看上去返回了多个值，实际上是先创建了一个元组然后返回的。 这个语法看上去比较奇怪，实际上我们使用的是
逗号来生成一个元组，而不是用括号。比如下面的：

>>> a = (1, 2) # With parentheses
>>> a
(1, 2)
>>> b = 1, 2   # Without parentheses
>>> b
(1, 2)
>>
"""
a = (1, 2)
b = 1, 2
print(a == b)