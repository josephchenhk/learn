# Spark/PySpark

* Ref: [Spark 2.2.x 中文文档](https://spark-reference-doc-cn.readthedocs.io/zh_CN/latest/programming-guide/quick-start.html)
## How in install pyspark

Refer to official website [Spark](https://spark.apache.org/downloads.html).

You can also simply install from `pip`:

```shell
$ pip install pyspark
```

## Spark Shell
Enter the spark shell
```shell
$ conda activate pyspark
$ pyspark
...
SparkSession available as 'spark'.
```

### Create a dataset (analogy to pandas `DataFrame`)

```python
# we have a README.md file with 3 lines (the last 0 just means end of file)
(pyspark)$ import os
(pyspark)$ os.system('cat README.md')
hello
BB
123
0

# we create a spark `DataFrame` from the above file
(pyspark)$ textFile = spark.read.text('README.md')

# we count the number of rows in this `DataFrame`
(pyspark)$ textFile.count()
3

# get the first row
(pyspark)$ textFile.first()
Row(value='hello')
```

### Filter a dataset

We could use `dataset.filter()` to obtain the desired
<t style="color:blue">rows</t>:

```python
(pyspark)$ lineWithB = textFile.filter(textFile.value.contains("B"))
(pyspark)$ lineWithB.count()
1
(pyspark)$ lineWithB.first()
Row(value='BB')
```

## What is Spark?
Spark是个通用的集群计算框架，通过将大量数据集计算任务分配到多台计算机上，提供高效内存计算。spark
操作是通过一个称作弹性分布式数据集(resilient distributed datasets, RDDs)的分布式数据框架进
行的。

Spark核心组件如下：

- Spark Core：包含Spark的基本功能；尤其是定义RDD的API、操作以及这两者上的动作。其他Spark的库
  都是构建在RDD和Spark Core之上的。
- Spark SQL：提供通过Apache Hive的SQL变体Hive查询语言（HiveQL）与Spark进行交互的API。每个
  数据库表被当做一个RDD，Spark SQL查询被转换为Spark操作。对熟悉Hive和HiveQL的人，Spark可以
  拿来就用。
- Spark Streaming：允许对实时数据流进行处理和控制。很多实时数据库（如Apache Store）可以处理实
  时数据。Spark Streaming允许程序能够像普通RDD一样处理实时数据。
- MLlib：一个常用机器学习算法库，算法被实现为对RDD的Spark操作。这个库包含可扩展的学习算法，比如
  分类、回归等需要对大量数据集进行迭代的操作。之前可选的大数据机器学习库Mahout，将会转到Spark，并
  在未来实现。
- GraphX：控制图、并行图操作和计算的一组算法和工具的集合。GraphX扩展了RDD API，包含控制图、创建
  子图、访问路径上所有顶点的操作。
