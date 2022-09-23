#include <stdio.h>
#include <stdint.h>

int summit(int a, int b) {
  return a + b;
}

int main() {
  int mya = 0xdead;
  int myb = 0xbeef;
  int sum = summit(mya, myb);
  return sum;
}
