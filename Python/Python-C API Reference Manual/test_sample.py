# -*- coding: utf-8 -*-
# @Time    : 3/6/2020 5:53 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test_sample.py
# @Software: PyCharm

# from sample import *
# spam_system, print_function, add_function, func1_function, func2_function, func3

from sampleclass import SampleClassName
from sampleclass2 import SampleClass2Name

def test_type():
    class A(object):
        pass

    a = A()

    print(type(a))                   # <class '__main__.test_type.<locals>.A'> 实例对象a的类型是A
    print(isinstance(a, A))          # True  a是A的实例对象
    print(isinstance(a, object))     # True  a同时也是object的实例对象
    print(isinstance(a, type))       # False a是一个实例对象，所以它不属于类型对象

    print(type(A))                   # <class 'type'>    类型对象A的类型是<class 'type'>
    print(A.__base__)                # <class 'object'>  类型对象A的父类是object，即它的base是<class 'object'>
    print(isinstance(A, object))     # True  A既是object的实例 ？？
    print(isinstance(A, type))       # True  A也是type的实例 ？？

    print(type(object))              # <class 'type'> 类型对象object的类型是<class 'type'>
    print(isinstance(object, type))  # True           类型对象object是type的实例（鸡生蛋）

    print(type(type))                # <class 'type'> 类型对象type的类型也是<class 'type'>
    print(isinstance(type, object))  # True           类型对象type也是object的实例（蛋生鸡）

# print(test_type())

# print(spam_system("ls -l"))
# print(print_function())
# print(add_function(2, 4))
# print(func1_function(1, "hello", (3,4)))
# print(func1_function(1, "hello", (3,4), 50))
# print(func2_function(1))
# print(func2_function(3, state="happy", action="sing", type="red bird"))
# print(func3(int, (1.234, )))
# print(func3(eval, ("2+3.1", )))

# s = SampleClassName()
# print(s)
# print(type(s), type(SampleClassName))
#
# # 这个会报错，noddy.Noddy 类不能被继承
# try:
#     class A(SampleClassName):
#         pass
# except Exception as e:
#     print(e)




s = SampleClass2Name("abc", "def", 12)
print(s, s.name())
print(type(s), type(SampleClass2Name))
print(s.number, s.first, s.last)

try:
    class A(SampleClass2Name):
        pass
except Exception as e:
    print(e)