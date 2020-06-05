# 介绍
embedding Python：将Python插入其他语言的application
extending Python：用C/C++去扩展Python的功能

## 编程标准
写的C代码扩展，需符合[PEP 7](https://www.python.org/dev/peps/pep-0007/)，才能符合条件整合进Python

## 包含文件
C代码的第一行，必须为如下语句：

```
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

以上代码隐含包括了如下C头文件：<stdio.h>, <string.h>, <errno.h>, <limits.h>, <assert.h> and <stdlib.h> (if available).

在 Python.h 中所有用户可见的变量，均以 **Py** 或 **_Py** 作为前缀。因此，用户自定义的变量，不应该使用这两种前缀。在MAC OS中，Python.h 的位置在 /System/Library/Frameworks/Python.framework/Versions/Current/include/python2.7/Python.h  

使用 extern "C"{} 指定让大括号中的内容 以 C 语言的方式进行编译 ; 这样才能在 C++ 中找到对应的 C 语言中的函数。

## 有用的Macros

* Py_STRINGIFY(x)：将x转换成 C string. 例如： Py_STRINGIFY(123) 返回 "123".

* PyDoc_STRVAR(name, str)：创建一个变量 name 用作 docstrings. 如果 Python 没有 docstrings，该值为空. 例如：PyDoc_STRVAR(pop_doc, "Remove and return the rightmost element.");

* PyDoc_STR(str)：创建一个 docstring （如果docstring 被disable了，就显示为空）。例如：PyDoc_STR("Returns the keys of the row.")

## 对象、类型和引用计数

Objects, Types and Reference Counts

在 Python/C API 里，所有的python对象，都是 PyObject*；注意只能用指针类型的PyObject，你不应该定义一个automatically或者static的PyObject，因为所有的python对象都是在堆（heap）里面的。**但有一个例外**，类型的对象一般定义为 static PyTypeObject。

所有python对象，均有type和reference count属性，即便是简单的int也不例外。对于常见的python类型，有相应的Macro去检查是否属于某一类型，如PyList_Check(a)会返回true，如果指向a的object是一个python list。


