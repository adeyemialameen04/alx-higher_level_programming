#include "Python.h"
/*
 * macro that replicates the functionality of pythonlist_size
 */
#define custom_py_size(op) (((PyVarObject *)(op))->ob_size)

/**
 * print_python_bytes - Prints information about python byte objects
 * @p: PyObject pointer to print info about
 */
void print_python_bytes(PyObject *p)
{
	int size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (assert(PyBytes_Check(p)), custom_py_size(p));
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %d bytes: ", size < 10 ? size : 10);
	for (i = 0; i < 10 && i < size + 1; i++)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	putchar('\n');
}
/**
 * print_python_list - Prints information about python objects
 * @p: PyObject pointer to print info about
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, py_list_size;
	PyObject *item;
	const char *item_type;
	PyListObject *list_object_cast;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	list_object_cast = (PyListObject *)p;
	py_list_size = custom_py_size(p);

	printf("[*] Size of the Python List = %d\n", (int)py_list_size);
	printf("[*] Allocated = %d\n", (int)list_object_cast->allocated);
	for (i = 0; i < py_list_size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		item_type = (((PyObject *)(item))->ob_type)->tp_name;
		printf("Element %d: %s\n", (int)i, item_type);
		if (strncmp(item_type, "bytes", 5) == 0)
			print_python_bytes(item);
	}
}
