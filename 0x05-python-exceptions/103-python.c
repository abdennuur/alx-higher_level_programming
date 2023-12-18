#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print the basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t sz, alc, ix;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sz = var->ob_size;
	alc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", alc);

	for (ix = 0; ix < sz; ix++)
	{
		type = list->ob_item[ix]->ob_type->tp_name;
		printf("Element %ld: %s\n", ix, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[ix]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[ix]);
	}
}

/**
 * print_python_bytes - Print the basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz, ix;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", sz);
	for (ix = 0; ix < sz; ix++)
	{
		printf("%02hhx", bytes->ob_sval[ix]);
		if (ix == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Print the basic info about Python float objects
 * @p: PyObject float object
 */
void print_python_float(PyObject *p)
{
	char *buff = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buff = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buff);
	PyMem_Free(buff);
}
