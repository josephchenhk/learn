# -*- coding: utf-8 -*-
# @Time    : 7/23/2019 6:40 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 8.24.py
# @Software: PyCharm
"""
8.24 让类支持比较操作


你想让某个类的实例支持标准的比较运算(比如>=,!=,<=,<等)，但是又不想去实现那一大丢的特殊方法。
装饰器 functools.total_ordering 就是用来简化这个处理的。 使用它来装饰一个来，你只需定义一个 __eq__() 方法， 外加其他
方法(__lt__, __le__, __gt__, or __ge__)中的一个即可。 然后装饰器会自动为你填充其它比较方法。
"""

from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                self.living_space_footage,
                self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))

h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))

houses = [h1, h2]

print('Is h1 bigger than h2?', h1 > h2)                # prints False
print('Is h1 smaller than h2?', h1 < h2)               # prints False
print('Is h2 greater than or equal to h1?', h2 >= h1)  # Prints True
print('Which one is biggest?', max(houses))            # Prints 'h1: 654 square foot Cape'
print('Which is smallest?', min(houses))               # Prints 'h1: 654 square foot Cape'