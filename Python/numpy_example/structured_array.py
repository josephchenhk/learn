# -*- coding: utf-8 -*-
# @Time    : 5/4/2023 8:50 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: structured_array.py

"""
Copyright (C) 2022 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the terms of the JXW license,
which unfortunately won't be written for another century.

You should have received a copy of the JXW license with this file. If not,
please write to: josephchenhk@gmail.com
"""

import numpy as np

# Create a structured data type with column names
dt = np.dtype([('name', np.str_, 20), ('age', np.int32), ('height', np.float64)])

# Create a NumPy ndarray with the structured data type
data = np.array(
    [('Alice', 25, 5.6), ('Bob', 30, 5.9), ('Charlie', 35, 6.1)],
    dtype=dt
)

# Access the columns using the column names
print(data['name'])
print(data['age'])
print(data['height'])
print(type(data))

################################################################################
print("#"*50)

from numpy.lib.recfunctions import append_fields

# Create a NumPy ndarray
data = np.array([[1, 2], [3, 4], [5, 6]])

# Define the column names as a list
column_names = ['col1', 'col2']

# Create a structured data type with column names
dt = np.dtype([(name, np.float64) for name in column_names])

# Convert the ndarray to a structured array with named fields
structured_data = np.empty(data.shape[0], dtype=dt)
for i, name in enumerate(column_names):
    structured_data[name] = data[:, i]

# Access the columns using the column names
print(structured_data['col1'])
print(structured_data['col2'])
print(type(structured_data))
