#include <iostream>
#include "typename.h"
#include <any>

int add(int i, int j) {
  std::cout << "add of two integers!\n";
  return i + j;
}

double add(double i, double j) {
  std::cout << "add of two doubles!\n";
  return i + j;
}

double add(double i, int j) {
  std::cout << "add of double/integer!\n";
  return i - j;
}

std::string add(std::string i, std::string j) {
  std::cout << "add of two strings!\n";
  return i + j;
}

int main() {
  std::cout << "auto i = add(5, 4);\n";
  auto i = add(5, 4);

  std::cout << "auto j = add(5.0, 4.0);\n";
  auto j = add(5.0, 4.0);

  std::cout << "auto k = add(5.0, 4);\n";
  auto k = add(5.0, 4);

  std::cout << "auto l = add('hello', ', world.');\n";
  auto l = add("hello", ", world.");

  std::cout << "i ( add(5, 4); ) is a " << type_name(i) << "\n";
  std::cout << "j ( add(5.0, 4.0); ) is a " << type_name(j) << "\n";
  std::cout << "l ( add('hello', ', world')) is a " << type_name(l) << "\n";
  return 0;
}
