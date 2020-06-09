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