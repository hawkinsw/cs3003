#include <iostream>

int add(int i, int j) {
  return i + j;
}

double add(double i, double j) {
  return i + j;
}

double add(double i, int j) {
  return i - j;
}

template <typename T>
T minimum(T a, T b) {
  return a < b ? a : b;
}

template <typename T>
void print_type(T v) {
  std::cout << "Oops: cannot determine type!\n";
}

template <>
void print_type(int) {
  std::cout << "Integer\n";
}

template <>
void print_type(double) {
  std::cout << "Double\n";
}

template <>
void print_type(std::string) {
  std::cout << "String\n";
}


int main() {
  auto i = add(5, 4);
  auto j = add(5.0, 4.0);
  auto k = add(5.0, 4);

  std::cout << "i (" << i << ") is a ";
  print_type(i);
  std::cout << "j (" << j << ") is a ";
  print_type(j);
  std::cout << "k (" << k << ") is a ";
  print_type(k);

  auto m = minimum(std::string("alpha"), std::string("beta"));
  std::cout << "m (" << m << ") is a ";
  print_type(m);

  auto n = minimum(5, 4);
  std::cout << "n (" << n << ") is a ";
  print_type(n);
}