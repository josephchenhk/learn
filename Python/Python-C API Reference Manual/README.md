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

The PyObject struct is defined as:

```angularjs
typedef struct {
     Py_ssize_t ob_refcnt;   /* object reference count */
     PyTypeObject* ob_type;  /* object type */
};
```

For example: if a given PyObject* points to a unicode object, then the ob_type field will be set to &PyUnicode_Type where PyUnicode_Type is the Python unicode type. This should be accessed through Py_TYPE().

## Abstract Object API

### Generic Object Functions
Most of the builtin Python functions have an Abstract Object API equivalent. Generally the name is the same except it is PyObject_ClassCase instead of alllowercase. For instance,

```
PyObject_GetAttr()
PyObject_SetAttr()
PyObject_Repr()
```

### Number Protocol
Unlike comparisons, there are different functions for all of the numeric operators. These are mostly named PyNumber_{Operator}, for example:

```
PyNumber_Add()
PyNumber_Subtract()
PyNumber_Multiply()
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

# Ref

1. [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)

2. [How to Write and Debug C Extension Module](https://llllllllll.github.io/c-extension-tutorial/)