#include "cpython.h"
/**
 * print_python_string - function that printd cpython strings
 * @p:- pointer to the object
 * Return:- Always 0
 */


void print_python_string(PyObject *p)
{
	PyUnicodeObject *unicode = (PyUnicodeObject *)p;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(unicode))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(unicode));
		printf("  value: %s\n", PyUnicode_AsUTF8(unicode));
	}
	else if (PyUnicode_IS_COMPACT(unicode))
	{
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", PyUnicode_GET_LENGTH(unicode));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(unicode, NULL));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
