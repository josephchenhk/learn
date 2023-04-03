# -*- coding: utf-8 -*-
# @Time    : 2/4/2023 8:33 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: sample1.py

"""
Copyright (C) 2022 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the terms of the JXW license,
which unfortunately won't be written for another century.

You should have received a copy of the JXW license with this file. If not,
please write to: josephchenhk@gmail.com
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import isnan, when, count, col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

# create a SparkSession
spark = SparkSession.builder.appName('unsupervised_learning').getOrCreate()


################################# Load data ####################################
# type(df) = pyspark.sql.dataframe.DataFrame
df = spark.read.csv("OHLCV.txt", header=True, inferSchema=True)

###################### Access specific row and column ##########################
# Select the *column* containing the element of interest
col_names = ["Close", "Volume"]
selected = df.select(col_names)

# Collect all *rows* into a list of Row objects
rows = selected.collect()

# Access element in the first row of the selected column
row_indicies = slice(1, 3)
# elements = [Row(Close=103.5, Volume=75000.0), Row(Close=108.0, Volume=150000.0)]
elements = rows[row_indicies]
print(elements)
row_idx = 2
# element_1 = 150000.0
element_1 = rows[row_idx]['Volume']
# element_2 = 150000.0
element_2 = rows[row_idx][1]
print(element_1, element_2, element_1 == element_2)

# Remove date and ticker columns
df = df.drop("date", "ticker")

# Drop rows with NaN values
df = df.na.drop()

# Assemble features vector: VectorAssembler is a PySpark transformer that is
# used to assemble multiple columns of a DataFrame into a single feature vector
# column
assembler = VectorAssembler(inputCols=df.columns, outputCol="features")
# type(data) = pyspark.sql.dataframe.DataFrame
# df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
# data.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'features']
data = assembler.transform(df)

# Train KMeans model
kmeans = KMeans(k=2, seed=1)
model = kmeans.fit(data)

# Make predictions
# type(predictions) = pyspark.sql.dataframe.DataFrame
predictions = model.transform(data)
predictions.show()
