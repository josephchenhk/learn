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

// 打印函数
static PyObject * print_function(PyObject *self)
{
    PyObject_Print(self, stdout, 0);
    printf("sample module print function\n");
    PyObject *b = Py_True;
    Py_INCREF(b);
    return b;
}

// 加法函数
static PyObject * add_function(PyObject *self, PyObject *args)
{
    int num1, num2;
    PyObject * result = NULL;
    if (!PyArg_ParseTuple(args, "nn:add_function_name", &num1, &num2)) {
       printf("传入参数错误！\n");
       return NULL;
    }
    result = PyLong_FromLong(num1+num2);
    return result;
}





/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"spam_system", (PyCFunction)spam_system, METH_VARARGS, "Revoke linux command"},
    {"print_function", (PyCFunction)print_function, METH_NOARGS, "Print something"},
    {"add_function", (PyCFunction)add_function, METH_VARARGS, "Add two integers"},
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
    printf("init sample module\n");
    return PyModule_Create(&samplemodule);
}