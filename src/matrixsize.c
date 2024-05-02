#include "matrixsize.h"
#include <stdio.h>

void get_matrix_size(int *rows, int *cols) {
    printf("Enter the number of rows in the matrix: ");
    scanf("%d", rows);
    printf("Enter the number of columns in the matrix: ");
    scanf("%d", cols);
}