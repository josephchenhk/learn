# -*- coding: utf-8 -*-
# @Time    : 4/5/2021 5:39 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: volatility_indicators.py
# @Software: PyCharm

"""
The average true range (ATR) is a technical analysis indicator, introduced by market technician J. Welles Wilder Jr. in
his book New Concepts in Technical Trading Systems, that measures market volatility by decomposing the entire range of
an asset price for that period.1


The true range indicator is taken as the greatest of the following:
    current high less the current low;
    the absolute value of the current high less the previous close;
    and the absolute value of the current low less the previous close.

The ATR is then a moving average, generally using 14 days, of the true ranges.
"""