#include <stdint.h>
#include <stdio.h>

int main() {
  int name[4] = {3, 4, 28, 32};

  printf("The address of name is %lx\n", (uintptr_t)&name);
  printf("The address of name[0] is %lx\n", (uintptr_t)&(name[0]));
  printf("The address of name[1] is %lx\n", (uintptr_t)&(name[1]));
  printf("The address of name[2] is %lx\n", (uintptr_t)&(name[2]));
  printf("The address of name[3] is %lx\n", (uintptr_t)&(name[3]));

  uintptr_t calculated_oned_index = (uintptr_t)(&name) + 3 * sizeof(int);
  printf("The calculated_oned_index is %lx\n", calculated_oned_index);

  if (calculated_oned_index == (uintptr_t)&name[3]) {
    printf("Yes, we calculated the 1D index correctly.\n");
  } else {
    printf("Oops, we calculated the 1D index incorrectly.\n");
  }

  printf("name[3]: %d\n", name[3]);
  printf("*calculated_oned_index: %d\n", *(int *)calculated_oned_index);

  unsigned int rows = 4;
  unsigned int cols = 4;
  int name_2d[rows][cols] = {
      {1, 2, 3, 4},
      {5, 6, 7, 8},
      {9, 10, 11, 12},
      {13, 14, 15, 16},
  };

  unsigned int twod_row = 1;
  unsigned int twod_col = 3;

  uintptr_t calculated_twod_index =
      (uintptr_t)(&name_2d) + (twod_row * cols + twod_col) * sizeof(int);

  if (calculated_twod_index == (uintptr_t)&name_2d[twod_row][twod_col]) {
    printf("Yes, we calculated the 2D index correctly.\n");
  } else {
    printf("Oops, we calculated the 2D index incorrectly.\n");
  }

  printf("The address of name_2d[%u][%u] is %lx\n", twod_row, twod_col,
         (uintptr_t)&(name_2d[twod_row][twod_col]));
  printf("The calculated_twod_index is %lx\n", calculated_twod_index);

  printf("The name_2d[%u][%u] is %d\n", twod_row, twod_col,
         name_2d[twod_row][twod_col]);
  printf("*calculated_twod_index: %d\n", *(int *)calculated_twod_index);

  return 0;
}
