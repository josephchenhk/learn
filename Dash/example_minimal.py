# -*- coding: utf-8 -*-
# @Time    : 29/3/2021 3:34 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: example_minimal.py
# @Software: PyCharm

import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.H1('My first Dash App!')

if __name__=="__main__":
    app.run_server()