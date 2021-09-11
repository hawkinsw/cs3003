#include <iostream>

int main() {
  int a, b, c;

  a = 1;
  b = 0;
  c = 0;

  /*
   * By the precedence and associativity 
   * rules of C++, this statement is true!
   * > is a binary operator that evaluates
   * with left-to-right associativity.
   *
   * https://en.cppreference.com/w/cpp/language/operator_precedence
   *
   * So, a > b evaluates first. That is an expression
   * that yields true. The resulting expression
   * is true > c. true is coerced into an
   * integer because C has mixed-mode operators but
   * the hardware does not. In other words, before
   * C++ will evaluate such an expression, it has to 
   * make the operand's two types the same. true's
   * value as an integer is 1. Therefore, the
   * statement becomes 1 > c and  c is 0. 1 > 0 
   * so the statement evaluates to true.
   *
   * Is this a surprising result?
   */
  if (a > b > c) {
    std::cout << "Yes, a > b > c\n";
  } else {
    std::cout << "No, a > b > c\n";
  }
  return 0;
}
