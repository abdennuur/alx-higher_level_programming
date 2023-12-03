#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int sz = PyList_Size(p);
	int ix;
	PyListObject *objct = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", objct->allocated);
	for (ix = 0; ix < sz; ix++)
		printf("Element %i: %s\n", ix, Py_TYPE(objct->ob_item[ix])->tp_name);
}
