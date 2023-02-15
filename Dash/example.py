# -*- coding: utf-8 -*-
# @Time    : 28/3/2021 4:32 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: example.py
# @Software: PyCharm

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()
    print("Done.")
