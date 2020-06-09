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

所有python对象，均有type和reference count属性，即便是简单的int也不例外。

### 类型
对于常见的python类型，有相应的Macro去检查是否属于某一类型，如PyList_Check(a)会返回true，如果指向a的object是一个python list。

### 引用计数
引用计数：counts how many different places there are that have a reference to an object. Such a place could be another object, or a global (or static) C variable, or a local variable in some C function.

如果引用计数变成零，该object就会被deallocate；如果还有其他对象引用该对象，删除其他对象时，引用计数就会递减，直至变成零。

手动操作引用计数：递增Py_INCREF()，和递减Py_DECREF()。

理论上，当一个变量指向一个对象时，对象的引用计数就应该 +1；当该变量goes out of scope的时候，引用计数就应该 -1。这样一进一出，刚好抵消，所以一般我们并不需要手动地去更新引用计数。然后，对于提取list元素出来的操作，要特别小心 （a common pitfall is to extract an object from a list and hold on to it for a while without incrementing its reference count. ）

最好的方式是使用默认的操作，即以Py开头的一些macro去处理对象（A safe approach is to always use the generic operations (functions whose name begins with PyObject_, PyNumber_, PySequence_ or PyMapping_). These operations always increment the reference count of the object they return. This leaves the caller with the responsibility to call Py_DECREF() when they are done with the result; this soon becomes second nature.）

### 创建一个tuple，list

方法一：
```
PyObject *t;

t = PyTuple_New(3);
PyTuple_SetItem(t, 0, PyLong_FromLong(1L));
PyTuple_SetItem(t, 1, PyLong_FromLong(2L));
PyTuple_SetItem(t, 2, PyUnicode_FromString("three"));
```

方法二：
```
PyObject *tuple, *list;

tuple = Py_BuildValue("(iis)", 1, 2, "three");
list = Py_BuildValue("[iis]", 1, 2, "three");
```

# PyObject

The PyObject struct is defined as

```
typedef struct {
    Py_ssize_t ob_refcnt;  /* object reference count */
    PyTyoeObject* ob_type; /* object type */
};
```

# Raise Exceptions

Python exceptions are very different from C++ exceptions. If you want to raise Python exceptions from your C extension module, then you can use the Python API to do so. Some of the functions provided by the Python API for exception raising are as follows:


|                   Function                          |                          Description                                                                                                                           |
|:---------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|PyErr_SetString(PyObject *type, const char *message) |	Takes two arguments: a PyObject * type argument specifying the type of exception, and a custom message to display to the user                                  |
|PyErr_Format(PyObject *type, const char *format)     |	Takes two arguments: a PyObject * type argument specifying the type of exception, and a formatted custom message to display to the user                        |
|PyErr_SetObject(PyObject *type, PyObject *value)	  | Takes two arguments, both of type PyObject *: the first specifies the type of exception, and the second sets an arbitrary Python object as the exception value |

## 定制化Exception

```angularjs
static PyObject *StringTooShortError = NULL;

PyMODINIT_FUNC PyInit_fputs(void) {
    /* Assign module value */
    PyObject *module = PyModule_Create(&fputsmodule);

    /* Initialize new exception object */
    StringTooShortError = PyErr_NewException("fputs.StringTooShortError", NULL, NULL);

    /* Add exception object to your module */
    PyModule_AddObject(module, "StringTooShortError", StringTooShortError);

    return module;
}
```

# 定义常量

两种方式：（1）通过PyModule_AddIntConstant去定义；（2）通过PyModule_AddIntMacro去定义。
```angularjs
PyMODINIT_FUNC PyInit_fputs(void) {
    /* Assign module value */
    PyObject *module = PyModule_Create(&fputsmodule);

    /* Add int constant by name */
    PyModule_AddIntConstant(module, "FPUTS_FLAG", 64);

    /* Define int macro */
    #define FPUTS_MACRO 256

    /* Add macro to module */
    PyModule_AddIntMacro(module, FPUTS_MACRO);

    return module;
}
```


# Ref

1. [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)

2. [How to Write and Debug C Extension Module](https://llllllllll.github.io/c-extension-tutorial/)