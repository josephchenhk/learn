# Spark/PySpark

## How in install pyspark

Refer to official website [Spark](https://spark.apache.org/downloads.html).

You can also install from `pip`:

```shell
$ pip install pyspark
```

### Use pyspark in ipython

```shell
# check existing profiles
$ ipython profile list
Available profiles in /Users/joseph/.ipython:
    default

# create a profile named `spark1` (you can specify anyname you like)
$ ipython profile create spark1
Unable to load extension: pydevd_plugins.extensions.types.pydevd_plugin_pandas_types
[ProfileCreate] Generating default config file: PosixPath('/Users/joseph/.ipython/profile_spark1/ipython_config.py')
[ProfileCreate] Generating default config file: PosixPath('/Users/joseph/.ipython/profile_spark1/ipython_kernel_config.py')
```

Now, in the `startup` folder under the home path:
`/Users/joseph/.ipython/profile_spark1/startup`, all the python scripts (`*.py`
and `*.ipy`) will be executed <t style="color:blue">**prior**</t> to the executing script, in
<t style="color:cyan">lexicographical</t> order:

```shell
$ ls /Users/joseph/.ipython/profile_spark1/startup
00-first.py
50-middle.py
99-last.ipy
```

The above shows that the scripts will be executed in the order of `00-first.py
--> 50-middle.py --> 99-last.ipy`.

So we just create a `py` file:

```shell
$ touch /Users/joseph/.ipython/profile_spark1/startup/00-pyspark-setup.py
```

and add the following code to it:

```python
import os
import sys

# Configure the environment
if 'SPARK_HOME' not in os.environ:
     os.environ['SPARK_HOME'] = '/srv/spark'

# Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

# Add the PySpark/py4j to the Python Path
sys.path.insert(0, os.path.join(SPARK_HOME, "python", "build"))
sys.path.insert(0, os.path.join(SPARK_HOME, "python"))
```

Now we start our IPython notebook that was just created:

```python
$ ipython notebook --profile spark
[TerminalIPythonApp] WARNING | File 'notebook' doesn't exist
```

Ok, we saw the error, and the solution is [here](https://stackoverflow.com/questions/44057601/ipython-notebook-will-not-start-on-command-line).

```shell
$ jupyter notebook --generate-config
Writing default config to: /Users/joseph/.jupyter/jupyter_notebook_config.py
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
