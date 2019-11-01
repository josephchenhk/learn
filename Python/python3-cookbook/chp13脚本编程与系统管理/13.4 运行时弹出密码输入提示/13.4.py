# -*- coding: utf-8 -*-
# @Time    : 10/31/2019 4:30 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.4.py
# @Software: PyCharm
"""
13.4 运行时弹出密码输入提示

"""

import getpass

user = getpass.getuser()
passwd = getpass.getpass()

def svc_login(user, passwd):
    if passwd=='123456':
        return True
    return False

if svc_login(user, passwd):
    print(f'Yay! User {user} login!')
else:
    print(f'Boo! User {user} fail to login!')