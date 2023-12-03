#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject
 *
 * Return: not
 */
void print_python_list_info(PyObject *p)
{
PyObject *itm;
PyListObject *lst = (PyListObject *)p;
int ix, sz, alc;

sz = Py_SIZE(p);
alc = lst->allocated;
printf("[*] Size of the Python List = %d\n", sz);
printf("[*] Allocated = %d\n", alc);

for (ix = 0; ix < sz; ix++)
{
itm =  PyList_GetItem(p, ix);
printf("Element %d: %s\n", ix, Py_TYPE(itm)->tp_name);
}
}
