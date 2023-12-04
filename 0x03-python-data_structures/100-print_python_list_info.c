#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Function that prints some basic
 *                          info about Python lists.
 * @p: Python list (PyObject pointer).
 */
void print_python_list_info(PyObject *p)
{
	int elem;

	/* Print the allocated memory */
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	/* Loop through each element and print its type name */
	for (elem = 0; elem < Py_SIZE(p); elem++)
	{
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
	}
}
