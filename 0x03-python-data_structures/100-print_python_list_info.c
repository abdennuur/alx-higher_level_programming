#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - Print basic info about Py lists
 * @p: PyObject
 *
 * Return: Not
 */
void print_python_list_info(PyObject *p)
{
PyObject *item;
PyListObject *list = (PyListObject *)p;
int ix, size, aloc;

size = Py_SIZE(p);
aloc = list->allocated;
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", aloc);

for (ix = 0; ix < size; ix++)
{
item =  PyList_GetItem(p, ix);
printf("Element %d: %s\n", ix, Py_TYPE(item)->tp_name);
}
}
