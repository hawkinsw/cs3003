#include <iostream>

int g(void) {
  int variable = 4;
  variable += variable;
  return variable;
}

int f(void) {
  static int variable = 4;
  variable += variable;
  return variable;
}

int main() {
  std::cout << "f(): " << f() << "\n";
  std::cout << "f(): " << f() << "\n";
  std::cout << "f(): " << f() << "\n";
  std::cout << "f(): " << f() << "\n";

  std::cout << "g(): " << g() << "\n";
  std::cout << "g(): " << g() << "\n";
  std::cout << "g(): " << g() << "\n";
  std::cout << "g(): " << g() << "\n";

  // Even though the `variable` in `f` is still alive (its lifetime
  // continues here), we cannot access it because it is not in scope.
  //
  // scope_ne_lifetime.cpp:29:32: error: use of undeclared identifier 'variable'
  // std::cout << "variable: " << variable << "\n"; 
  return 0;
}
