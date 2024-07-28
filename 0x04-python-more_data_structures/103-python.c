#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
* print_python_list - Prints basic info about Python lists
* @p: A PyObject list
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, alloc, i;
const char *type;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = ((PyVarObject *)p)->ob_size;
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", alloc);

for (i = 0; i < size; i++)
{
type = (Py_TYPE(PyList_GetItem(p, i)))->tp_name;
printf("Element %zd: %s\n", i, type);
if (strcmp(type, "bytes") == 0)
print_python_bytes(PyList_GetItem(p, i));
}
}

/**
* print_python_bytes - Prints basic info about Python bytes objects
* @p: A PyObject bytes object
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *string;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", string);
printf("  first %zd bytes:", size + 1 > 10 ? 10 : size + 1);

for (i = 0; i < size + 1 && i < 10; i++)
printf(" %02x", (unsigned char)string[i]);
printf("\n");
}
