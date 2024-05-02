# cimpl.pyx

cdef extern from "solver.h":
    void row_reduce(double** matrix, int rows, int cols)

def row_reduce(matrix, rows, cols):
    cdef int i, j
    cdef double **arr = <double **> malloc(rows * sizeof(double *))
    for i in range(rows):
        arr[i] = <double *> malloc(cols * sizeof(double))
        for j in range(cols):
            arr[i][j] = matrix[i][j]
    row_reduce(arr, rows, cols)
