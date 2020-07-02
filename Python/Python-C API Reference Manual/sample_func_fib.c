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
//        printf("b=%lu\n", b);
    }

    return b;
}

static PyObject*
pyfib(PyObject* self, PyObject* n)
{
    unsigned long as_unsigned_long = PyLong_AsUnsignedLong(n);
    if(PyErr_Occurred()){
//        PyErr_SetString(PyExc_ValueError, "Parameter passed in is not a valid integer!");

        PyObject* repr = PyObject_Repr(n);
        PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
        const char *bytes = PyBytes_AS_STRING(str);
        Py_XDECREF(repr);
        Py_XDECREF(str);
        PyErr_Format(PyExc_ValueError, "Parameter %s passed in is not a valid integer!", bytes);
        return NULL;
    }
    PyObject *result = PyLong_FromUnsignedLong(cfib(as_unsigned_long));
    return result;
}

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


static PyObject*
pyfib_parsearg(PyObject* self, PyObject* args, PyObject* kwargs)
{
    /* the names of the arguments as a static array */
    static char* keywords[] = {"n", NULL};

    PyObject* n;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "O", keywords, &n)) {
        /* the arguments passed don't correspond to the signature
           described */
        return NULL;
    }

    unsigned long as_unsigned_long = PyLong_AsUnsignedLong(n);
    if(PyErr_Occurred()){
//        PyErr_SetString(PyExc_ValueError, "Parameter passed in is not a valid integer!");
        PyObject* repr = PyObject_Repr(n);
        PyObject* str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
        const char *bytes = PyBytes_AS_STRING(str);
        Py_XDECREF(repr);
        Py_XDECREF(str);
        PyErr_Format(PyExc_ValueError, "Parameter %s passed in is not a valid integer!", bytes);
        return NULL;
    }
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
        "fib_pyobj",                /* The name as a C string. */
        (PyCFunction) pyfib_pyobj,  /* The C function to invoke. */
        METH_O,                     /* Flags telling Python how to invoke ``pyfib`` */
        fib_doc,                    /* The docstring as a C string. */
    },
    {
        "fib_parsearg",                /* The name as a C string. */
        (PyCFunction) pyfib_parsearg,  /* The C function to invoke. */
        METH_VARARGS | METH_KEYWORDS,  /* Flags telling Python how to invoke ``pyfib`` */
        fib_doc,                       /* The docstring as a C string. */
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