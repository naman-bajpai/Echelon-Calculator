#include "solver.h"
#include <stdio.h>

void row_reduce(double **matrix, int rows, int cols) {
    printf("Row reduced echelon form of the matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%.2f ", matrix[i][j]);
        }
        printf("\n");
    }
}
