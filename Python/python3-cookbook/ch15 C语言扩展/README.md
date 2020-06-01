Ref

1. [Python3.X使用C Extensions调用C/C++](https://juejin.im/entry/5c808beff265da2dab17f886)

用PyArg_ParseTuple函数将Python类型的参数转为C语言中的数据类型：

|   字符 |   C语言类型        |  Python                         |
|:-----:|:----------------:|:-------------------------------:|
|  c    |   char           | 长度为1的字符串转为C语言的字符        |
|  s    |   char array     | Python中字符串转为C语言字符数组      |
|  d    |   double         | Python中float转为C语言中double     |
|  f    |   float          | Python中float转为C语言中float      |
|  i    |   int            | Python中int转为C语言中int          |
|  l    |   long           | Python中int转为C语言中long         |
|  o    |   PyObject*      | Python中的类对象转为C语言中PyObject  |

与函数PyArg_ParseTuple相反，函数Py_BuildValue将C语言中的数据类型转为Python对象，类型映射关系是一致的，看几个简单例子如下。

|   示例代码                                |  转为Python对象       |
|:---------------------------------------:|:--------------------:|
|  Py_BuildValue("s", "AB")               |   "AB"               |
|  Py_BuildValue("i", 1000)               |   1000               |
|  Py_BuildValue("(iii)", 1, 2, 3)        |   (1, 2, 3)          |
|Py_BuildValue("{si,si}", "a", 4, "b", 9) |   {"a": 4, "b": 9}   |
|  Py_BuildValue("")                      |   None               |

定义的PyMethodDef用于登记转换的函数列表;

定义的PyModuleDef用于Module名称及其中的函数列表;

PyMODINIT_FUNC用于指定初试化入口函数，其中PyModule_Create用于创建模块.

调用setup.py，即输入如下命令：

python setup.py build_ext --inplace
其中，--inplace表示在源码处生成pyd文件。执行上面命令后，会得到如下文件。

demo.cp36-win_amd64.pyd