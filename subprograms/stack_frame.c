#include <stdio.h>

int max(int left, int right) {
  int local_left = left;
  int local_right = right;

  if (local_left > local_right) {
    return local_left;
  }
  return local_right;
}

int sum(int alpha, int beta) {
  int local_alpha = alpha;
  int local_beta = beta;
  int mmax = max(local_alpha, local_beta);
  return mmax + beta;
}

int main() {
  int result = sum(5, 7);
  printf("result: %d\n", result);
  return 0;
}
