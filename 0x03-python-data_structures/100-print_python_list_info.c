#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function that prints basic info about Python lists
 * @p: pyobject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *el = PyList_GetItem(p, i);
		PyObject *type = PyObject_Type(el);
		const char *name = Py_TYPE(el)->tp_name;

		printf("Element %ld: %s\n", i, name);
		Py_DECREF(type);
	}
}
