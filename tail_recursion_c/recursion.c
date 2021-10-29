#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>

uint64_t fibonacci(uint64_t a) {
  if (a == 0) {
    assert(false);
    return 0;
  }
  if (a == 1) {
    assert(false);
    return 1;
  }
  return fibonacci(a - 1) + fibonacci(a - 2);
}

uint64_t fibonacci_tail(uint64_t a, uint64_t minus1, uint64_t minus2) {
  if (a == 2) {
    assert(false);
    return minus1 + minus2;
  }
  if (a == 1) {
    assert(false);
    return minus1;
  }
  if (a == 0) {
    assert(false);
    return minus2;
  }
  return fibonacci_tail(a - 1, minus1 + minus2, minus1);
}

uint64_t fibonacci_iter(uint64_t a) {
  uint64_t minus1 = 1;
  uint64_t minus2 = 0;
  for (; a > 2; a--) {
    uint64_t old_minus1 = minus1;
    minus1 += minus2;
    minus2 = old_minus1;
  }
  return minus1 + minus2;
}

uint64_t main() {
  // printf("fibonacci of 50: %lu\n", fibonacci(50));
  printf("fibonacci of 50: %lu\n", fibonacci_tail(50, 1, 0));
  return 0;
}
