#include <Python.h>
#include <stdio.h>

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list.
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, allocated, i;
PyObject *item;

if (!PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
print_python_bytes(item);
else if (PyFloat_Check(item))
print_python_float(item);
}
}

/**
* print_python_bytes - Prints basic info about Python bytes.
* @p: A PyObject bytes.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);

printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
for (i = 0; i < size + 1 && i < 10; i++)
printf(" %02x", (unsigned char)str[i]);
printf("\n");
}

/**
* print_python_float - Prints basic info about Python floats.
* @p: A PyObject float.
*/
void print_python_float(PyObject *p)
{
double value;

if (!PyFloat_Check(p))
{
printf("[ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);

printf("[.] float object info\n");
printf("  value: %f\n", value);
}
