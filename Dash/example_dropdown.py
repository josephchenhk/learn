# -*- coding: utf-8 -*-
# @Time    : 29/3/2021 3:41 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: example_dropdown.py
# @Software: PyCharm

import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('Selection'),
        html.Br(),
        dcc.Dropdown(
            options=[
                {'label': 'option 1', 'value': 1},
                {'label': 'option 2', 'value': 2},
                {'label': 'option 3', 'value': 3}
            ]
        )
    ]
)

if __name__=="__main__":
    app.run_server()
