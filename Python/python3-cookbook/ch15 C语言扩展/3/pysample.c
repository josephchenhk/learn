#include "Python.h"
#include "sample.h"

/*
为了能让接受和处理数组具有可移植性，你需要使用到 Buffer Protocol

*/

static PyObject *py_avg(PyObject *self, PyObject *args) {
    PyObject *bufobj;
    Py_buffer view;
    double result;
    /* 将Python Object转换成C语言的Object */
    if (!PyArg_ParseTuple(args, "O", &bufobj)) {
        return NULL;
    }

    /* PyBuffer_GetBuffer() 函数。 给定一个任意的Python对象，它会试着去获取底层内存信息，它简单的抛出一个异常并返回-1 */
    if (PyObject_GetBuffer(bufobj, &view, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {
        return NULL;
    }

    /*
    对于数组、字节字符串和其他类似对象而言，一个 Py_buffer 结构体包含了所有底层内存的信息。 它包含一个指向内存地址、大小、元素大小、
    格式和其他细节的指针。下面是这个结构体的定义：
    typedef struct bufferinfo {
        void *buf;              // Pointer to buffer memory
        PyObject *obj;          // Python object that is the owner
        Py_ssize_t len;         // Total size in bytes
        Py_ssize_t itemsize;    // Size in bytes of a single item
        int readonly;           // Read-only access flag
        int ndim;               // Number of dimensions
        char *format;           // struct code of a single item
        Py_ssize_t *shape;      // Array containing dimensions
        Py_ssize_t *strides;    // Array containing strides
        Py_ssize_t *suboffsets; // Array containing suboffsets
    } Py_buffer;
    */
    if (view.ndim != 1) {
        PyErr_SetString(PyExc_TypeError, "Expected a 1-dimensional array");
        PyBuffer_Release(&view);
        return NULL;
    }

    /* Check the type of items in the array */
    if (strcmp(view.format,"d") != 0) {
        PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
        PyBuffer_Release(&view);
        return NULL;
    }

    /* Pass the raw buffer and size to the C function */
    result = avg(view.buf, view.shape[0]);

    /* Indicate we're done working with the buffer */
    PyBuffer_Release(&view);
    return Py_BuildValue("d", result);
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"avg",  py_avg, METH_VARARGS, "Return average"},
    { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,

    "sample",           /* name of module */
    "A sample module",  /* Doc string (may be NULL) */
    -1,                 /* Size of per-interpreter state or -1 */
    SampleMethods       /* Method table */
};

/* Module initialization function */
/* 在解释器中注册模块对象 */
PyMODINIT_FUNC PyInit_sample(void) {
    return PyModule_Create(&samplemodule);
}