#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Function to print python bytes info
 * @p: PyObject.
 * return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &size);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		size = 10;
	printf("  first %ld bytes: ", size + 1);
	for (i = 0; i < size; i++)
		printf("%02x ", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_list - Function to print python lists info
 * @p: PyObject.
 * return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, len, allocated;
	PyObject *oj;
	const char *type;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	len = PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < len; i++)
	{
		oj = PyList_GET_ITEM(p, i);
		type = Py_TYPE(oj)->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check(oj))
			print_python_bytes(oj);
	}
}
