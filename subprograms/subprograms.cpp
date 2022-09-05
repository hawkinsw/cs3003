#include <iostream>
#include "typename.h"
#include <any>

class NotComparable {
  public:
  explicit NotComparable(double value) : m_value(value) {}

  explicit operator std::any() {
    std::cout << "Converting to std::any\n";
    return std::any(*this);
  }

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

/*
template <typename T>
T minimum(T a, T b) {
  return a < b ? a : b;
}
*/
std::any minimum(std::any a, std::any b) {
  std::cout << "In std::any version of minimum\n";
  return a;
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
  std::cout << "k ( add(5.0, 4); ) is a " << type_name(k) << "\n";
  std::cout << "l ( add('hello', ', world')) is a " << type_name(l) << "\n";

  auto m = minimum(std::string("alpha"), std::string("beta"));
/*
  std::cout << "m (" << m << ") is a " << type_name(m) << "\n";

  auto n = minimum(5, 4);
  std::cout << "n (" << n << ") is a " << type_name(n) << "\n";

  */
  std::any testing = static_cast<std::any>(NotComparable(5));
  auto o = minimum(static_cast<std::any>(NotComparable(5)), NotComparable(6));

  //std::cout << "o (" << o << ") is a " << type_name(o) << "\n";
}
