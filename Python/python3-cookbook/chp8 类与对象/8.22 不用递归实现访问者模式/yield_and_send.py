# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 4:43 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: yield_and_send.py
# @Software: PyCharm
"""
python的yield与send实例详解
"""
def gener(num):
    while True:
        print("0:before yield num is: %d" % num)
        num = yield
        print("1:after yield num is %d" % num)
    print("exc end")

g = gener(1)          # 什么也不会输出
g.send(None)          # 会输出  0:before yield num is: 1
print("goto loop")
for i in range(5):
    print("---loop---")
    print(">>>>send back:" + str(g.send(i)))  # 再次send, 会接着yield之后的语句执行, 即会输出  1:after yield num is 0

"""
0:before yield num is: 1
goto loop
---loop---
1:after yield num is 0
0:before yield num is: 0
>>>>send back:None
---loop---
1:after yield num is 1
0:before yield num is: 1
>>>>send back:None
---loop---
1:after yield num is 2
0:before yield num is: 2
>>>>send back:None
---loop---
1:after yield num is 3
0:before yield num is: 3
>>>>send back:None
---loop---
1:after yield num is 4
0:before yield num is: 4
>>>>send back:None
"""

"""
generator函数调用后，第一次send(None)，generator执行到yield之前，之后每次调用send(), 从yield所在行开始执行，运行到片段
结尾或再次遇到yield， generator从yield中接受参数，如果yield后有表达式，则返回表达式的值，类似return关键字的功能。yield
关键字保存了generator每次的执行状态。

>>>>send back:不再是None，而是有一个具体的数值了
"""
def gener2(num):
    while True:
        print("0:before yield num is: %d" % num)
        num = yield num**2 # 代码唯一有变化的地方
        print("1:after yield num  is %d" % num)
    print("exc end")

print("--------------------------------------\n")
g2 = gener2(2)
print(">>>>send back:" + str(g2.send(None)))
print(">>>>send back:" + str(g2.send(3)))