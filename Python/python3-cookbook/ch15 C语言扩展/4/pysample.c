#include "Python.h"
#include "sample.h"

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



///* 定义一个Point结构体 */
//typedef struct Point {
//    double x,y;
//} Point;


/* Destructor function for points */
static void del_Point(PyObject *obj) {
    free(PyCapsule_GetPointer(obj,"Point"));
}


/* 将一个(PyObject *)转换成Point */
static Point *PyPoint_AsPoint(PyObject *obj) {
    return (Point *) PyCapsule_GetPointer(obj, "Point");
}


/* 将一个(Point *)转换成 (PyObject *) */
static PyObject *PyPoint_FromPoint(Point *p, int must_free) {
    return PyCapsule_New(p, "Point", must_free ? del_Point : NULL);
}


/* Create a new Point object */
static PyObject *py_Point(PyObject *self, PyObject *args) {
    Point *p;
    double x,y;
    if (!PyArg_ParseTuple(args,"dd",&x,&y)) {
        return NULL;
    }
    p = (Point *) malloc(sizeof(Point));
    p->x = x;
    p->y = y;
    return PyPoint_FromPoint(p, 1);
}

static PyObject *py_mydistance(PyObject *self, PyObject *args) {
    Point *p1, *p2;
    PyObject *py_p1, *py_p2;
    double result;

    if (!PyArg_ParseTuple(args,"OO",&py_p1, &py_p2)) {
    return NULL;
    }
    if (!(p1 = PyPoint_AsPoint(py_p1))) {
    return NULL;
    }
    if (!(p2 = PyPoint_AsPoint(py_p2))) {
    return NULL;
    }
    result = mydistance(p1,p2);
    return Py_BuildValue("d", result);
}







/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"consume_iterable",  py_consume_iterable, METH_VARARGS, "Print Python iterable"},
    {"mydistance",  py_mydistance, METH_VARARGS, "Distance"},
    {"Point",  py_Point, METH_VARARGS, "Point"},
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