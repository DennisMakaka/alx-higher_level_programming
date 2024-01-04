#ifdef PYTHON_TEST_DRIVEN_DEVELOPMENT_H
#define PYTHON_TEST_DRIVEN_DEVELOPMENT_H

#include <Python.h>

// Function prototypes for Python Test Driven Development project
void print_python_string(PyObject *p);
void add_integer(int a, int b);
void say_my_name(char *first_name, char *last_name);
void print_square(int size);
void text_indentation(char *text);
void matrix_mul(int **m_a, int **m_b);
void lazy_matrix_mul(int **m_a, int **m_b);
void matrix_divided(int **matrix, int div);

#endif /* PYTHON_TEST_DRIVEN_DEVELOPMENT_H */
