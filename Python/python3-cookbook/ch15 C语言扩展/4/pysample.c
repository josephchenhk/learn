#include "Python.h"

/*
输入一个Python iterable，在c语言里将之处理每一个元素（打印出来）

*/

static PyObject *py_consume_iterable(PyObject *self, PyObject *args) {
    PyObject *obj;
    PyObject *iter;
    PyObject *item;
    int value;

    if (!PyArg_ParseTuple(args, "O", &obj)) {
        return NULL;
    }
    if ((iter = PyObject_GetIter(obj)) == NULL) {
        return NULL;
    }
    while ((item = PyIter_Next(iter)) != NULL) {
        /* Use item */

        // This PyObject seems to be a PyInt as PyInt_Check returns 1
        assert(PyInt_Check(item) == 1);
        // Now the only way i found to convert this PyInt to a [C] int is:
        value = (int) PyLong_AsLong(item);
        // Print out the int
        printf("Obtain %d\n", value);

        Py_DECREF(item);
    }

    Py_DECREF(iter);
    return Py_BuildValue("");
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"consume_iterable",  py_consume_iterable, METH_VARARGS, "Print Python iterable"},
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