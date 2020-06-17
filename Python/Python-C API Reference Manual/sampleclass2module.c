#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>

/*
定义一个类（class），这一节我们将对这个类进行扩展，添加属性、方法，并且支持子类。
*/

// 记录实例对象的数据：修改 noddy_NoddyObject 结构体，为其添加三个字段
typedef struct {
    PyObject_HEAD
    /* Type-specific fields go here. */
    PyObject * first; /* first name */
    PyObject * last;  /* last name */
    int number;
} noddy_NoddyObject;


// 定义自己的new方法，为对象分配内存空间
static PyObject * Noddy_new(PyTypeObject * type, PyObject * args, PyObject * kwds)
{
    noddy_NoddyObject * self;
    self = (noddy_NoddyObject *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->first = PyUnicode_FromString("");
        if (self->first == NULL)
        {
          Py_DECREF(self);
          return NULL;
        }
        self->last = PyUnicode_FromString("");
        if (self->last == NULL)
        {
          Py_DECREF(self);
          return NULL;
        }
        self->number = 0;
    }
    return (PyObject *)self;
}


// 定义init方法，为类对象进行实例化
static int Noddy_init(noddy_NoddyObject * self, PyObject * args, PyObject * kwds)
{
    PyObject * first=NULL, * last=NULL, * tmp;
    static char *kwlist[] = {"first", "last", "number", NULL};

    if (! PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                      &first, &last,
                                      &self->number))
        return -1;

    if (first) {
        tmp = self->first;
        Py_INCREF(first);
        self->first = first;
        Py_XDECREF(tmp);
    }

    if (last) {
        tmp = self->last;
        Py_INCREF(last);
        self->last = last;
        Py_XDECREF(tmp);
    }
    return 0;
}


// 由于对象包含了几项数据，因此在对象销毁时需要先释放数据的资源。定义资源释放方法：
static void Noddy_dealloc(noddy_NoddyObject * self)
{
    Py_XDECREF(self->first);
    Py_XDECREF(self->last);
    Py_TYPE(self)->tp_free((PyObject *)self);
}


// 为该类定义一个方法用于返回该对象的first值和last值
static PyObject * Noddy_name(noddy_NoddyObject * self)
{
    static PyObject * format = NULL;
    PyObject * args, * result;
    if (format == NULL) {
        format = PyUnicode_FromString("%s %s");
        if (format == NULL)
            return NULL;
    }
    if (self->first == NULL) {
        PyErr_SetString(PyExc_AttributeError, "first");
        return NULL;
    }
    if (self->last == NULL) {
        PyErr_SetString(PyExc_AttributeError, "last");
        return NULL;
    }
    args = Py_BuildValue("OO", self->first, self->last);
    if (args == NULL)
        return NULL;
    result = PyUnicode_Format(format, args);
    Py_DECREF(args);
    return result;
}


// 定义好方法，在后面定义类的时候调用
static PyMethodDef Noddy_methods[] = {
    {"name", (PyCFunction)Noddy_name, METH_NOARGS, "Return the name, combining the first and last name"},
    {NULL}  /* Sentinel */
};


/* 虽然在noddy_NoddyObject结构体中定义了这几个字段，但是它们仍然在Python中是不可见的。
为了能在Python中访问这几个属性，需要设置noddy_NoddyType的tp_members字段。*/
static PyMemberDef Noddy_members[] = {
    {"first", T_OBJECT_EX, offsetof(noddy_NoddyObject, first), 0, "first name"},
    {"last", T_OBJECT_EX, offsetof(noddy_NoddyObject, last), 0, "last name"},
    {"number", T_INT, offsetof(noddy_NoddyObject, number), 0, "noddy number"},
    {NULL}  /* Sentinel */
};


// 定义类
static PyTypeObject noddy_NoddyType = {
//    PyObject_HEAD_INIT(NULL)
    PyVarObject_HEAD_INIT(NULL, 0)
//    0,                         /*ob_size*/
    "noddy.Noddy",             /*tp_name*/
    sizeof(noddy_NoddyObject), /*tp_basicsize*/
    0,                         /*tp_itemsize*/
    (destructor)Noddy_dealloc, /*tp_dealloc*/
    0,                         /*tp_print*/
    0,                         /*tp_getattr*/
    0,                         /*tp_setattr*/
    0,                         /*tp_compare*/
    0,                         /*tp_repr*/
    0,                         /*tp_as_number*/
    0,                         /*tp_as_sequence*/
    0,                         /*tp_as_mapping*/
    0,                         /*tp_hash*/
    0,                         /*tp_call*/
    0,                         /*tp_str*/
    0,                         /*tp_getattro*/
    0,                         /*tp_setattro*/
    0,                         /*tp_as_buffer*/
    Py_TPFLAGS_DEFAULT |
    Py_TPFLAGS_BASETYPE,       /*tp_flags*/
    "Noddy objects",           /*tp_doc*/
    0,                         /*tp_traverse */
    0,                         /*tp_clear */
    0,                         /*tp_richcompare */
    0,                         /*tp_weaklistoffset */
    0,                         /*tp_iter */
    0,                         /*tp_iternext */
    Noddy_methods,             /*tp_methods */
    Noddy_members,             /*tp_members */
    0,                         /*tp_getset */
    0,                         /*tp_base */
    0,                         /*tp_dict */
    0,                         /*tp_descr_get */
    0,                         /*tp_descr_set */
    0,                         /*tp_dictoffset */
    (initproc)Noddy_init,      /*tp_init */
    0,                         /*tp_alloc */
    Noddy_new,                 /*tp_new */
};









//
static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,

    "sampleclass2",           /* name of module */
    "A sample module",  /* Doc string (may be NULL) */
    -1,                 /* Size of per-interpreter state or -1 */
    Noddy_methods       /* Method table */
};


//
PyMODINIT_FUNC PyInit_sampleclass2(void)
{
    PyObject* m;

    noddy_NoddyType.tp_new = Noddy_new;
    if (PyType_Ready(&noddy_NoddyType) < 0)
        return NULL;

    m = PyModule_Create(&samplemodule);

    Py_INCREF(&noddy_NoddyType);
    PyModule_AddObject(m, "SampleClass2Name", (PyObject *)&noddy_NoddyType); // 在python中调用时，s = SampleClassName()

    return m;
}