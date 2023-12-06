#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int ix = 0;

	for (; ix < n - 1; ++ix)
		printf("%02x ", (unsigned char) str[ix]);

	printf("%02x", str[ix]);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *cl = (PyBytesObject *) p;
	int c_bytes, cl_size = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(cl))
	{
		cl_size = PyBytes_Size(p);
		c_bytes = cl_size + 1;

		if (c_bytes >= 10)
			c_bytes = 10;

		printf("  size: %d\n", cl_size);
		printf("  trying string: %s\n", cl->ob_sval);
		printf("  first %d bytes: ", c_bytes);
		print_hexn(cl->ob_sval, c_bytes);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *p)
{
	int ix = 0, ls_len = 0;
	PyObject *itm;
	PyListObject *cl = (PyListObject *) p;

	printf("[*] Python list info\n");
	ls_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", ls_len);
	printf("[*] Allocated = %d\n", (int) cl->allocated);

	for (; ix < ls_len; ++ix)
	{
		itm = PyList_GET_ITEM(p, ix);
		printf("Element %d: %s\n", ix, itm->ob_type->tp_name);

		if (PyBytes_Check(itm))
			print_python_bytes(itm);
	}
}
