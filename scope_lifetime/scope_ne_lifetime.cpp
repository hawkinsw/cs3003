#include <iostream>

void f(void) {
  static int variable = 4;
}

int main() {
  f();
  return 0;
}
