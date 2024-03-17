#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Function to print python lists info
 * @p: Pyobject.
 * return: None
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *ll;
	int i;

	ll = (PyListObject *)p;

	printf("[*] Size of the Python list = %ld\n", ll->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);

	for (i = 0; i < ll->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
