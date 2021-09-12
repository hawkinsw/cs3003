#include <iostream>
#include "typename.h"

class NotComparable {
  public:
  explicit NotComparable(double value) : m_value(value) {}

  friend std::ostream &operator<<(std::ostream &os, const NotComparable &nc);

/*
  bool operator<(const NotComparable &other) {
    std::cout << "Calling operator<\n";
    return this->m_value < other.m_value;
  }
*/
  private:
  double m_value;

};
std::ostream &operator<<(std::ostream &os, const NotComparable &nc) {
  os << "nc's m_value: " << nc.m_value;
  return os;
}

template <>
std::string type_name(NotComparable) {
  return "NotComparable";
}

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

int main() {
  auto i = add(5, 4);
  auto j = add(5.0, 4.0);
  auto k = add(5.0, 4);

  std::cout << "i (" << i << ") is a " << type_name(i) << "\n";
  std::cout << "j (" << j << ") is a " << type_name(j) << "\n";
  std::cout << "k (" << k << ") is a " << type_name(k) << "\n";

  auto m = minimum(std::string("alpha"), std::string("beta"));
  std::cout << "m (" << m << ") is a " << type_name(m) << "\n";

  auto n = minimum(5, 4);
  std::cout << "n (" << n << ") is a " << type_name(n) << "\n";

/*
  auto o = minimum(NotComparable(5), NotComparable(6));
  std::cout << "o (" << o << ") is a " << type_name(o) << "\n";
*/
}
