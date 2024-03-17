#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Function to print python lists info
 * @p: Pyobject.
 * return: None
 */
void print_python_list_info(PyObject *p)
{
	int i, len, allocated;
	PyObject *oj;

	len = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < len; i++)
	{
		printf("Element %d: ", i);

		oj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(oj)->tp_name);
	}
}
