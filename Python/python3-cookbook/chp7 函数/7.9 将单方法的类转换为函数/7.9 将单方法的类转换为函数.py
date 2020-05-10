# -*- coding: utf-8 -*-
# @Time    : 7/24/2019 2:30 PM
# @Author  : Joseph Chen
# @Email   : joseph.chen@magnumwm.com
# @FileName: 7.9 将单方法的类转换为函数.py
# @Software: PyCharm
"""
7.9 将单方法的类转换为函数


** 一个除了 __init__ 之外，只包含一个方法的类，等价于一个闭包函数 **
"""

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        # return urlopen(self.template.format_map(kwargs))  # wow, format_map的用法，之前没怎么用过，很fancy
        return self.template.format_map(kwargs)             # yahoo finance no longer works anymore

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
# for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
#     print(line.decode('utf-8'))
print(yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'))


"""
大部分情况下，你拥有一个单方法类的原因是需要存储某些额外的状态来给方法使用。 比如，定义UrlTemplate类的唯一目的就是先
在某个地方存储模板值，以便将来可以在open()方法中使用。

使用一个内部函数或者闭包的方案通常会更优雅一些。简单来讲，一个闭包就是一个函数， 只不过在函数内部带上了一个额外的变量
环境。闭包关键特点就是它会记住自己被定义时的环境。 因此，在我们的解决方案中，opener() 函数记住了 template 参数的值，
并在接下来的调用中使用它。

任何时候只要你碰到需要给某个函数增加额外的状态信息的问题，都可以考虑使用闭包。 相比将你的函数转换成一个类而言，闭包
通常是一种更加简洁和优雅的方案。
"""

def urltemplate(template):
    def opener(**kwargs):
        return template.format_map(kwargs)  # 这里template作为一个参数传进来，达到和self.template同样的效果
    return opener                           # 闭包

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
print(yahoo(names='IBM,AAPL,FB', fields='sl1c1v'))  # 将上面的 yahoo.open(...) 改为 yahoo(...)