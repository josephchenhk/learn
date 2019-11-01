# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 9:43 AM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 13.9.py
# @Software: PyCharm

"""
13.9 通过文件名查找文件

"""

import os

def findfile(start, name):
    for relpath, dirs, files in os.walk(start):

        print(f"""
        realpath: {relpath},
        dirs: {dirs},
        files: {files}\n
        """)

        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
    # findfile(sys.argv[1], sys.argv[2])
    start = os.path.dirname(os.path.realpath(__file__))
    name = 'file1.1.txt'
    name = '13.9.py'
    print(start)
    findfile(start, name)