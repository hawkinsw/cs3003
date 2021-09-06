#include <iostream>

void f() {
  for (int i = 0; i<10; i++) {
    std::cout << "i: " << i << "\n";
  }

  // The following statement will cause a compilation error
  // because i is local to the code in the body of the for
  // loop.
  // std::cout << "i: " << i << "\n";
}

int main() {
  f();
}

/*
 * Expected output:
    $ ./a.out
    i: 0
    i: 1
    i: 2
    i: 3
    i: 4
    i: 5
    i: 6
    i: 7
    i: 8
    i: 9
 */
