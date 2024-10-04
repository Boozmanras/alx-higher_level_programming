#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
* print_python_string - Prints information about Python strings
* @p: PyObject string object
* Description: Prints string information (length, value, type)
*/
void print_python_string(PyObject *p)
{
const char *type;
Py_ssize_t length;
wchar_t *value;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);
value = PyUnicode_AsWideCharString(p, &length);

if (PyUnicode_IS_COMPACT_ASCII(p))
type = "compact ascii";
else
type = "compact unicode object";

printf("  type: %s\n", type);
printf("  length: %ld\n", length);
printf("  value: %ls\n", value);

PyMem_Free(value);
}
