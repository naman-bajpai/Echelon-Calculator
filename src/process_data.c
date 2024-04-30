#include <stdio.h>
#include <stdlib.h>

double process_data(const char *filename) {
  
  FILE *file = fopen(filename, "r");
  if (file == NULL) {
    printf("Error opening file.\n");
    return -1.0; // Indicate error
  }

  double sum = 0.0;
  int count = 0;
  double value;
  while (fscanf(file, "%lf", &value) == 1) {
    sum += value;
    count++;
  }
  
  if (count == 0) {
      printf("Empty file\n");
      fclose(file);
      return -1.0; // Indicate error
  }
  
  double mean = sum / count;
  fclose(file);
  return mean;
}
