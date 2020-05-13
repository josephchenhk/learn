# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 2:00 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.11.py
# @Software: PyCharm

"""
13.11 给简单脚本增加日志功能

"""

import logging

def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()