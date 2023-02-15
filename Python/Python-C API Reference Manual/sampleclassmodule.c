#define PY_SSIZE_T_CLEAN
#include <Python.h>


/*
定义一个类（class）
*/

// 记录实例对象的数据
typedef struct {
    PyObject_HEAD
    /* Type-specific fields go here. */
} sampleObject;

// 定义一个类
static PyTypeObject sampleType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0) // PyVarObject_HEAD_INIT(NULL, 0)
    "SampleClass",             /*tp_name*/
    sizeof(sampleObject),      /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    0,                         /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash */
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT,        /*tp_flags*/
    "Sample objects",          /*tp_doc*/
};



static PyMethodDef SampleMethods[] = {
    {NULL}  /* Sentinel */
};

static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,

    "sampleclass",           /* name of module */
    "A sample module",  /* Doc string (may be NULL) */
    -1,                 /* Size of per-interpreter state or -1 */
    SampleMethods       /* Method table */
};

PyMODINIT_FUNC PyInit_sampleclass(void)
{
    PyObject* m;

    sampleType.tp_new = PyType_GenericNew;
    if (PyType_Ready(&sampleType) < 0)
        return NULL;

    m = PyModule_Create(&samplemodule);

    Py_INCREF(&sampleType);
    PyModule_AddObject(m, "SampleClassName", (PyObject *)&sampleType); // 在python中调用时，s = SampleClassName()

    return m;
}
