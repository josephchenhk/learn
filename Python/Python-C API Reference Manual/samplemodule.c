#define PY_SSIZE_T_CLEAN
#include <Python.h>

// 调用linux命令，用system(command)
static PyObject * spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);       // example of command：ls -l
    return PyLong_FromLong(sts); // 经过PyLong_FromLong处理，c type的int类型被转换成PyObject *类型了
}


/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"spam_system", (PyCFunction)spam_system, METH_VARARGS, "Revoke linux command"},
    { NULL, NULL, 0, NULL}
};

/* Module structure */
//PyDOC_STRVAR(sample_doc, "A sample module");
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