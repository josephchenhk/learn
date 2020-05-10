# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 11:34 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.5 定义有默认参数的函数.py
# @Software: PyCharm
"""
7.5 定义有默认参数的函数

定义一个有可选参数的函数是非常简单的，直接在函数定义中给参数指定一个默认值，并放到参数列表最后就行了.
"""

def spam(a, b=42):
    print(a, b)

spam(1)    # Ok. a=1, b=42
spam(1, 2) # Ok. a=1, b=2

"""
需要测试某个可选参数是否被使用者传递进来。 这时候需要小心的是你不能用某个默认值比如None、 0或者False值来测试用户提供的值(因为这些值都是合法的值，
是可能被用户传递进来的)。 因此，你需要其他的解决方案了。

为了解决这个问题，你可以创建一个独一无二的私有对象实例object()
"""
_no_value = object()
def spam(a, b=_no_value):
    if b is _no_value:
        print("No b param was passed in,", a)
    else:
        print(f"b={b} was passed in as a param: ", a, b)

spam(1)           # No b param was passed in, 1
spam(1, 2)        # b=2 was passed in as a param:  1 2
spam(1, object()) # b=<object object at 0x1145739b0> was passed in as a param:  1 <object object at 0x1145739b0>
spam(1, _no_value)# No b param was passed in, 1
