# -*- coding: utf-8 -*-
# @Time    : 3/1/2022 11:06 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test1.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

"""
>> pip install python-telegram-bot==13.9
"""

import telegram

from Credentials import TELEGRAM_TOKEN

bot = telegram.Bot(token=TELEGRAM_TOKEN)
print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

print("Done.")
