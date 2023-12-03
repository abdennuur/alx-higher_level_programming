#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about a python list
 * @p: PyObject
 * 
 *Return: void 
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p) ->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i);

		obj =  PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
