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
    return b; // return True; if want to return None: Py_BuildValue("");
}

// 加法函数
static PyObject * add_function(PyObject *self, PyObject *args)
{
    int num1, num2;
    PyObject * result = NULL;
    if (!PyArg_ParseTuple(args, "nn:add_function_name", &num1, &num2)) {
       printf("传入参数错误！\n");
       return NULL; // invoke an error in Python
    }
    result = PyLong_FromLong(num1+num2);
    return result;
}

// 传入参数，解释成一个Python字典
static PyObject* func1_function(PyObject *self, PyObject *args)
{
    int num, i, j;
    long lnum=0;   // 可选参数，如果不传入，就默认值是0
    const char* s1 = NULL;
    PyObject *obj = NULL;
    if (!PyArg_ParseTuple(args, "is(ii)|l",
                          &num, &s1, &i, &j, &lnum)) {
        printf("func1_function:传入参数错误！\n");
        return NULL;
    }
    printf("num: %d\tstr1: %s\n"
           "i: %d\tj: %d\tlnum: %ld\n",
           num, s1, i, j, lnum);

    obj = Py_BuildValue("{sisisislss}",
                        "num", num, "i", i, "j", j, "lnum", lnum, "s1", s1);
    return obj;
}

// 传入列表参数和关键字参数（可选）
static PyObject* func2_function(PyObject *self, PyObject *args, PyObject *kwargs)
{
    int voltage;
    char *state = "a stiff";
    char *action = "voom";
    char *type = "Norwegian Blue";

    static char *kwlist[] = {"voltage", "state", "action", "type", NULL}; // NULL作为结束标志

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "i|sss", kwlist,
                                     &voltage, &state, &action, &type)){
        printf("func2_function:传入参数错误！\n");
        return NULL;
    }

    printf("-- This parrot wouldn't %s if you put %i Volts through it.\n",
           action, voltage);
    printf("-- Lovely plumage, the %s -- It's %s!\n", type, state);
    Py_INCREF(Py_None);
    return Py_None;
}

// 在扩展模块中调用Python方法
static PyObject* func3_function(PyObject *self, PyObject *args)
{
    PyObject *my_callback = NULL;
    PyObject *result = NULL;
    PyObject *arg = NULL;
    if (!PyArg_ParseTuple(args, "OO:set_callback;argument;", &my_callback, &arg)) {
        printf("传入参数错误！\n");
        return NULL;
    }
    if (!PyCallable_Check(my_callback)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be callable");
        return NULL;
    }
    result = PyObject_CallObject(my_callback, arg);
    if (!result) {
        Py_INCREF(Py_None);
        result = Py_None;
    }
    return result;
}










/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"spam_system", (PyCFunction)spam_system, METH_VARARGS, "Revoke linux command"},
    {"print_function", (PyCFunction)print_function, METH_NOARGS, "Print something"},
    {"add_function", (PyCFunction)add_function, METH_VARARGS, "Add two integers"},
    {"func1_function", (PyCFunction)func1_function, METH_VARARGS, "Pass in params and return a dict"},
    {"func2_function", (PyCFunction)func2_function, METH_VARARGS | METH_KEYWORDS, "Pass in args and kwargs params"},
    {"func3", (PyCFunction)func3_function, METH_VARARGS, NULL},
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
