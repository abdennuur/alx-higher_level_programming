#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print info about python list
 * @p: --PyObject--
 * 
 *Return: (void) 
 */

void print_python_list_info(PyObject *p)
{
    long int sz, ix;
    PyListObject *ls;
    PyObject *itm;

    sz = Py_SIZE(p);
    printf("[*] Size of the Python List = %ld\n", sz);

    lst = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", lst->allocated);

    for (ix = 0; ix < sz; ix++)
    {
        itm = PyList_GetItem(p, ix);
        printf("Element %ld: %s\n", ix, Py_TYPE(itm)->tp_name);
    }
}
