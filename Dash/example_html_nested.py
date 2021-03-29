# -*- coding: utf-8 -*-
# @Time    : 29/3/2021 3:37 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: example_html_nested.py
# @Software: PyCharm

import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('Header 1'),
        html.H1('Header 1'),
        html.P(['Test', html.Br(), 'Test Again']),
        html.Table(
            html.Tr(
                [
                    html.Td('First col'),
                    html.Td('Second col')
                ]
            )
        )
    ]
)

if __name__=="__main__":
    app.run_server()