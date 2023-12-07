#define PY_SSIZE_T_CLEAN

#define EPS_C 1e-7

#include <math.h>
#include "../python3.12/Python.h"


static PyObject *method_add(PyObject *self, PyObject *args) {
  PyObject *arg1 = NULL;
  PyObject *arg2 = NULL;
  PyObject *result = NULL;

  if (!PyArg_ParseTuple(args, "OO", &arg1, &arg2)) {
    PyErr_SetString(PyExc_TypeError, "Invalid arguments");
  } else if (PyLong_Check(arg1) && PyLong_Check(arg2)) {
    long x = PyLong_AsLong(arg1);
    long y = PyLong_AsLong(arg2);
    result = Py_BuildValue("l", x + y);
  } else if (PyFloat_Check(arg1) && PyFloat_Check(arg2)) {
    double a = PyFloat_AsDouble(arg1);
    double b = PyFloat_AsDouble(arg2);
    result = Py_BuildValue("d", a + b);
  } else {
    PyErr_SetString(PyExc_TypeError, "Invalid argument types");
  }
  return result;
}
// ************************************************************************************

static PyObject *method_sub(PyObject *self, PyObject *args) {
  PyObject *arg1 = NULL;
  PyObject *arg2 = NULL;
  PyObject *result = NULL;

  if (!PyArg_ParseTuple(args, "OO", &arg1, &arg2)) {
    PyErr_SetString(PyExc_TypeError, "Invalid arguments");
  } else if (PyLong_Check(arg1) && PyLong_Check(arg2)) {
    long x = PyLong_AsLong(arg1);
    long y = PyLong_AsLong(arg2);
    result = Py_BuildValue("l", x - y);
  } else if (PyFloat_Check(arg1) && PyFloat_Check(arg2)) {
    double a = PyFloat_AsDouble(arg1);
    double b = PyFloat_AsDouble(arg2);
    result = Py_BuildValue("d", a - b);
  } else {
    PyErr_SetString(PyExc_TypeError, "Invalid argument types");
  }
  return result;
}
// ************************************************************************************

static PyObject *method_mul(PyObject *self, PyObject *args) {
  PyObject *arg1 = NULL;
  PyObject *arg2 = NULL;
  PyObject *result = NULL;

  if (!PyArg_ParseTuple(args, "OO", &arg1, &arg2)) {
    PyErr_SetString(PyExc_TypeError, "Invalid arguments");
  } else if (PyLong_Check(arg1) && PyLong_Check(arg2)) {
    long x = PyLong_AsLong(arg1);
    long y = PyLong_AsLong(arg2);
    result = Py_BuildValue("l", x * y);
  } else if (PyFloat_Check(arg1) && PyFloat_Check(arg2)) {
    double a = PyFloat_AsDouble(arg1);
    double b = PyFloat_AsDouble(arg2);
    result = Py_BuildValue("d", a * b);
  } else {
    PyErr_SetString(PyExc_TypeError, "Invalid argument types");
  }
  return result;
}
// ************************************************************************************

static PyObject *method_div(PyObject *self, PyObject *args) {
  PyObject *arg1 = NULL;
  PyObject *arg2 = NULL;
  PyObject *result = NULL;

  if (!PyArg_ParseTuple(args, "OO", &arg1, &arg2)) {
    PyErr_SetString(PyExc_TypeError, "Invalid arguments");
  } else if ((PyLong_Check(arg1) && PyLong_Check(arg2)) || 
    (PyFloat_Check(arg1) && PyFloat_Check(arg2))) {
    double a = PyFloat_AsDouble(arg1);
    double b = PyFloat_AsDouble(arg2);
    if (EPS_C > fabs(b)) {
      PyErr_SetString(PyExc_ZeroDivisionError, "division by zero");
    } else {
      result = Py_BuildValue("d", a / b);
    }
  } else {
    PyErr_SetString(PyExc_TypeError, "Invalid argument types");
  }
  return result;
}

// ************************************************************************************

static PyMethodDef BinOperMethods[] = {
  { "add", method_add, METH_VARARGS, "py interface to add two numbers" },
  { "sub", method_sub, METH_VARARGS, "py interface to substract two numbers" },
  { "mul", method_mul, METH_VARARGS, "py interface to multiply two numbers" },
  { "div", method_div, METH_VARARGS, "py interface to divide two numbers" },
  {NULL, NULL, 0, NULL}
};
// ************************************************************************************

static struct PyModuleDef math_methods = {
  PyModuleDef_HEAD_INIT,
  "math_methods",
  "addition, substraction, multiplication, division",
  -1,
  BinOperMethods
};
// ************************************************************************************

PyMODINIT_FUNC PyInit_math_methods(void) {
  return PyModule_Create(&math_methods);
};
// ************************************************************************************


