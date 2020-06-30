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