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

## C Level Representation of Python Structures

一个 PyObject 结构体的定义如下（非常简单，仅包含一个refcount，和一个PyTypeObject指针）:

```angularjs
typedef struct {
     Py_ssize_t ob_refcnt;   /* object reference count */
     PyTypeObject* ob_type;  /* object type */
};
```

ob_type指向PyTypeObject指针。For example: if a given PyObject* points to a unicode object, then the ob_type field will be set to &PyUnicode_Type where PyUnicode_Type is the Python unicode type. This should be accessed through Py_TYPE().

ob_refcnt类似一个整数，计算该object被引用的次数。The ob_refcnt is the reference count of the object. This is the number of places where this object is being used. This should be accessed through Py_REFCNT(). The reference count can be increased with Py_INCREF() or decreased with Py_DECREF(). As soon as the reference count reaches zero, the object is no longer needed and it will be deallocated.


### Concrete types
PyObject* is an abstract reference that can point to any type; however, we eventually need to actually store information on an object. Subtypes of object are represented by structs whose first member is a PyObject followed by any instance data needed.

In C, a pointer to a struct is equivalent to a pointer to its first member, this makes it safe to cast from a type defined this way to and from PyObject*.

For example, a sub-type of PyObject (PyLongObject):
```
typedef struct {
     Py_ssize_t ob_refcnt;   /* object reference count */
     PyTypeObject* ob_type;  /* object type */

     XXX                     /* some values */
}PyLongObject;
```

## Writing a New Function in C

It is important to declare all functions as static. This is normally good practice in C but it is especially important when linking with CPython which is a very large project. We don’t want to pollute the namespace. (refer [here](https://blog.csdn.net/guotianqing/article/details/79828100) for static in C)

```
/* sample_func_fib.c file */

#include "Python.h"

static unsigned long
cfib(unsigned long n)
{
    unsigned long a = 1;
    unsigned long b = 1;
    unsigned long c;

    if (n <= 1) {
        return 1;
    }

    while (--n > 1) {
        c = a + b;
        a = b;
        b = c;
    }

    return b;
}

static PyObject*
pyfib(PyObject* self, PyObject* n)
{
    unsigned long as_unsigned_long = PyLong_AsUnsignedLong(n);
    PyObject *result = PyLong_FromUnsignedLong(cfib(as_unsigned_long));
    return result;
}

PyDoc_STRVAR(fib_doc, "computes the nth Fibonacci number");
PyMethodDef methods[] = {
    {
        "fib",                /* The name as a C string. */
        (PyCFunction) pyfib,  /* The C function to invoke. */
        METH_O,               /* Flags telling Python how to invoke ``pyfib`` */
        fib_doc,              /* The docstring as a C string. */
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }  /* sentinel */
};

PyDoc_STRVAR(fib_module_doc, "provides a Fibonacci function");
PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "fib",
    fib_module_doc,
    -1,
    methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC
PyInit_fib(void)
{
    return PyModule_Create(&module);
}
```

For our function we only accept a single argument as a PyObject* so we can use the METH_O flag. For a list of the available flags see: [PyMethodDef.ml_flags](https://llllllllll.github.io/c-extension-tutorial/appendix.html#c.PyMethodDef.ml_flags).

With our function and module defined, we need to tell CPython how to import our module. To do that we need to define a single function with type PyMODINIT_FUNC named PyInit_{name} where name is the name of our module.


## Building and Importing

编写setup文件 (与sample_func_fib.c 放在同目录下)
```
# setup.py file
from setuptools import setup, find_packages, Extension

setup(
    name='fib',
    version='0.1.0',
    packages=find_packages(),
    license='GPL-2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    ext_modules=[
        Extension(
            # the qualified name of the extension module to build
            'fib',
            # the files to compile into our module relative to ``setup.py``
            ['sample_func_fib.c'],
        ),
    ],
)
```

在命令行下编译：
```commandline
$ python setup.py build_ext --inplace
```

导入使用
```
# test_sample_func_fib.py file
from fib import fib

print(fib(4))
```

## Error Handling

C不像Python一样有Error的处理。

### Global Exception Indicator

CPython uses three variables to store the state of the current exception. These hold the type of the current exception, the value of the current exception, and the Python traceback of the current exception. This is like an enhanced errno.

These values can be set or queried with the PyErr_* family of functions.

### Propagating Errors
In the CPython API, a NULL value is never valid for a PyObject* so it is used to signal that an error has occurred. For example: PyLong_FromUnsignedLong() returns a PyObject*; however, when memory cannot be allocated a PyExc_MemoryError is set and NULL is returned.

This is the most common error sentinel and is used for PyCFunctions.

### Raising Exceptions

To explicitly set the error indicator we can use one of PyErr_SetString() or PyErr_Format(). These functions take an exception type and either a message or a message format string and raise the given Python exception. After setting the exception, we need to clean up our references and then return NULL or some other sentinel to indicate that our function failed.

There are also helpers for raising common exceptions like: PyErr_NoMemory().

### Standard Exceptions
All of the builtin exceptions are accessible in C with a naming scheme of PyExc_{Name} where Name is the name as it appears in Python. For example:

PyExc_IndexError is the same as IndexError from within Python.

A full list of exceptions can be found here: https://docs.python.org/3.6/c-api/exceptions.html#standard-exception

## Abstract Object API

### Generic Object Functions
Most of the builtin Python functions have an Abstract Object API equivalent. Generally the name is the same except it is PyObject_ClassCase instead of alllowercase. For instance,

```
PyObject_GetAttr()
PyObject_SetAttr()
PyObject_Repr()
```

A weird quirk of the CPython API is that all of the comparison operators (>, >=, ==, etc...) are grouped into a single function called PyObject_RichCompare() instead of different functions like in Python. This is probably done to save space in the PyTypeObject struct.

PyObject_RichCompare() can invoke arbitrary Python code so we need to check for errors. This will also raise an error if a and b cannot be compared because they are incompatible types. Another one is PyObject_RichCompareBool() which returns a C int instead of a PyObject*. This saves us the hassle of worrying about cleaning up the reference to result. For example:
```
/ * 需要记得derefcount */
PyObject* a;  /* ... */
PyObject* b;  /* ... */

PyObject* result = PyObject_RichCompare(a, b, Py_LE);
if (!result) {
    /* error handling */
}
/* do stuff with ``result`` */
Py_DECREF(result);



/ * 不需要考虑derefcount */
PyObject* a;  /* ... */
PyObject* b;  /* ... */

int result = PyObject_RichCompareBool(a, b, Py_LE);
if (result < 0) {
    /* error handling */
}
```

### Number Protocol
Unlike comparisons, there are different functions for all of the numeric operators. These are mostly named PyNumber_{Operator}, for example:

```
PyNumber_Add()
PyNumber_Subtract()
PyNumber_Multiply()
```

One nice thing about Python int objects is that they can hold arbitrarily large integers. This is not true for unsigned long values which can store at most 2 ** 64 - 1. The Fibonacci sequence grows quickly and we will run out of room to store the results if we represent it as an unsigned long.

Our fib function can be rewritten as below:

```
/* 完全用PyObject去implement fib函数 */
static PyObject *
pyfib_pyobj(PyObject* self, PyObject *n)
{
    PyObject *a;
    PyObject *b;
    PyObject *c;
    PyObject *one;

//    printf("n is long: %d\n", PyLong_Check(n));

    a = PyLong_FromLong(1L);
    b = PyLong_FromLong(1L);
    one = PyLong_FromLong(1L);

    PyObject* result = PyObject_RichCompare(n, one, Py_LE);

    if (!result) {
        /* error handling */
        PyErr_SetString(PyExc_ValueError, "Can not compare!");
        return NULL;
    }
    /* do stuff with ``result`` */
//    printf("%d", PyObject_IsTrue(result));
    if(PyObject_IsTrue(result)){
        return one;
    }

    /* dereference */
    Py_DECREF(result);

//    printf("OK\n");
    n = PyNumber_Subtract(n, one);
    while (PyObject_IsTrue(PyObject_RichCompare(n, one, Py_GT))) {
        c = PyNumber_Add(a, b);
        a = b;
        b = c;
//        printf("b=%ld\n", PyLong_AsLong(b));
        n = PyNumber_Subtract(n, one);
    }

    Py_DECREF(a);
    Py_DECREF(b);
    Py_DECREF(one);

    return b;
}
```

## Fancy Argument Parsing
As a first pass, we could replace the METH_O in our PyMethodDef structure with METH_VARARGS | METH_KEYWORDS. This tell CPython to pass us three arguments:

```
PyObject* self: The module or instance.
PyObject* args: A tuple of positional arguments.
PyObject* kwargs: A dictionary of keyword arguments or NULL if no keyword arguments are provided. The dict can also be empty.
```
Now we can parse the arguments as below:

```
static PyObject*
pyfib(PyObject* self, PyObject* args, PyObject* kwargs) {
    /* the names of the arguments as a static array */
    static char* keywords[] = {"n", NULL};

    PyObject* n;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "O", keywords, &n)) {
        /* the arguments passed don't correspond to the signature
           described */
        return NULL;
    }

    /* ... */
}
```

We also need to update our PyMethodDef to look like (replace METH_O with METH_VARARGS | METH_KEYWORDS):

```
PyMethodDef methods[] = {
    {"fib", (PyCFunction) pyfib, METH_VARARGS | METH_KEYWORDS, fib_doc},
    {NULL},
};
```

### Type Conversion & Naming our Function
One nice feature of PyArg_ParseTupleAndKeywords() is that it can convert PyObject*s into C types for us.

```
static PyObject*
add(PyObject* self, PyObject* args, PyObject* kwargs)
{
    static char* keywords[] = {"a", "b", NULL};

    int a;
    int b;

    if (!PyArg_ParseTupleAndKeywords(args,
                                     kwargs,
                                     "ii:add",  // 解析成两个整数，报错时标明函数名称：TypeError: add() takes at most 2 arguments (3 given)
                                     keywords,
                                     &a,
                                     &b)) {
        return NULL;
    }

    return PyLong_FromLong(a + b);
}
```

### Optional Arguments
PyArg_ParseTupleAndKeywords() also supports optional arguments with the | special character.

```
static PyObject*
add(PyObject* self, PyObject* args, PyObject* kwargs)
{
    static char* keywords[] = {"a", "b", NULL};

    int a;
    int b = 1;

    if (!PyArg_ParseTupleAndKeywords(args,
                                     kwargs,
                                     "i|i", // 意味这第二个param是optional的
                                     keywords,
                                     &a,
                                     &b)) {
        return NULL;
    }

    return PyLong_FromLong(a + b);
}
```

### Keyword Only Arguments

PyArg_ParseTupleAndKeywords() supports keyword only arguments with the $ special character.

```
static PyObject*
add(PyObject* self, PyObject* args, PyObject* kwargs)
{
    static char* keywords[] = {"a", "b", NULL};

    int a;
    int b = 1;

    if (!PyArg_ParseTupleAndKeywords(args,
                                     kwargs,
                                     "i$i", // 意味这第二个param一定要是keyword argument
                                     keywords,
                                     &a,
                                     &b)) {
        return NULL;
    }

    return PyLong_FromLong(a + b);
}
```

## Writing a New Class in C
对于built-in方法和自定义方法，处理的方式各不相同：built-in方法可以通过相应的接口去转换：

```
__getattr__: PyTypeObject.tp_getattro
__setattr__: PyTypeObject.tp_setattro
__call__: PyTypeObject.tp_call
...
```

对于非built-in方法，通过字典PyTypeObject.tp_dict 去管理。

### Instance Data

通常，我们通过定义一个struct去定义一个新的类（class）：

```
typedef struct {
    PyObject base;             /* the base object values */
    PyObject* list_field;      /* a pointer to our list member */
    Py_ssize_t ssize_t_field;  /* our Py_ssize_t member */
    const char* string_field;  /* our const char* member */
} myobject;
```

### Slots Without a Python Equivalent

#### Allocation and Deallocation

在python，我们在内存建立一个实例，是通过调用 `object.__new__()`；如前所述，对应的CPython API是调用`PyTypeObject.tp_new`，这背后其实是调用`PyTypeObject.tp_alloc`去内存开辟一个地方储存self。

其实，我们除了`PyTypeObject.tp_new`之外，可以用如下两个更灵活的方法去操控内存的分配：

```
PyTypeObject.tp_alloc
PyTypeObject.tp_free
```

#### Garbage Collection
当发生循环引用，导致引用计数永远无法清零时，CPython API提供以下两个方法去处理：

1. `PyTypeObject.tp_traverse`：用于探测循环引用

2. `PyTypeObject.tp_clear`：用于解除循环引用，并清空该object的所有引用（从而可被回收）

#### Flags

`PyTypeObject.tp_flags`对type进行侦测（a bitmask of boolean values），比较常见的bits有 `Py_TPFLAGS_HAVE_GC`（该对象有垃圾回收机制，即遵循通常的引用计数），`Py_TPFLAGS_LONG_SUBCLASS`（该对象是`PyLongObject`的子对象）

当定义一个新的type的时候，一般总是先指明tpflags（通常是`Py_TPFLAGS_DEFAULT`）

### Defining a `PyTypeObject`

```
// 这里定义了Queue类的实例数据
typedef struct {
     PyObject q_base;       /* 或者可以PyObject_HEAD（表示该类型占用内存大小是固定的如int，float），或者可以PyObject_VAR_HEAD（表示该类型占用的内存是可变的如list，dict），storage for our type and reference count */
     Py_ssize_t q_maxsize;  /* the maximum number of elements in q_elements */
     PyObject* q_elements;  /* the elements in the queue as a Python list */
 } queue;


//这是一个Queue类，保存了该类的元信息
static PyTypeObject queue_type = {
     PyVarObject_HEAD_INIT(&PyType_Type, 0)
     "queue.Queue",                              /* tp_name */
     sizeof(queue),                              /* tp_basicsize */
     0,                                          /* tp_itemsize */
     (destructor) queue_dealloc,                 /* tp_dealloc */
     0,                                          /* tp_print */
     0,                                          /* tp_getattr */
     0,                                          /* tp_setattr */
     0,                                          /* tp_reserved */
     (reprfunc) queue_repr,                      /* tp_repr */
     0,                                          /* tp_as_number */
     0,                                          /* tp_as_sequence */
     0,                                          /* tp_as_mapping */
     0,                                          /* tp_hash */
     0,                                          /* tp_call */
     0,                                          /* tp_str */
     0,                                          /* tp_getattro */
     0,                                          /* tp_setattro */
     0,                                          /* tp_as_buffer */
     Py_TPFLAGS_DEFAULT |
     Py_TPFLAGS_HAVE_GC,                         /* tp_flags */
     queue_doc,                                  /* tp_doc */
     (traverseproc) queue_traverse,              /* tp_traverse */
     (inquiry) queue_clear,                      /* tp_clear */
     0,                                          /* tp_richcompare */
     0,                                          /* tp_weaklistoffset */
     0,                                          /* tp_iter */
     0,                                          /* tp_iternext */
     queue_methods,                              /* tp_methods */
     0,                                          /* tp_members */
     0,                                          /* tp_getset */
     0,                                          /* tp_base */
     0,                                          /* tp_dict */
     0,                                          /* tp_descr_get */
     0,                                          /* tp_descr_set */
     0,                                          /* tp_dictoffset */
     0,                                          /* tp_init */
     0,                                          /* tp_alloc */
     (newfunc) queue_new,                        /* tp_new */
};
```

PyType_Ready将方法load进来：
```
PyMODINIT_FUNC PyInit_sampleclass2(void)
{
    PyObject* m;

    noddy_NoddyType.tp_new = Noddy_new;
    if (PyType_Ready(&noddy_NoddyType) < 0)
        return NULL;

    m = PyModule_Create(&samplemodule);

    Py_INCREF(&noddy_NoddyType);
    PyModule_AddObject(m, "SampleClass2Name", (PyObject *)&noddy_NoddyType); // 在python中调用时，s = SampleClassName()

    return m;
}
```


你有三种方式处理掉一个引用：
1. 将引用传递给别人
2. 将引用存储起来
3. 调用 Py_DECREF()


```
// 编译方式1：
>>> python setup.py build_ext --inplace

// 编译方式2：
>>> python setup.py build
```

# Ref

1. [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)

2. [How to Write and Debug C Extension Module](https://llllllllll.github.io/c-extension-tutorial/)
