# 介绍
embedding Python：将Python插入其他语言的application
extending Python：用C/C++去扩展Python的功能

## 编程标准
写的C代码扩展，需符合PEP 7，才能符合条件整合进Python

## 包含文件
C代码的第一行，必须为如下语句：

```
#define PY_SSIZE_T_CLEAN
#include <Python.h>
```

以上代码隐含包括了如下C头文件：<stdio.h>, <string.h>, <errno.h>, <limits.h>, <assert.h> and <stdlib.h> (if available).

在 Python.h 中所有用户可见的变量，均以 **Py** 或 **_Py** 作为前缀。因此，用户自定义的变量，不应该使用这两种前缀。

使用 extern "C"{} 指定让大括号中的内容 以 C 语言的方式进行编译 ; 这样才能在 C++ 中找到对应的 C 语言中的函数。

