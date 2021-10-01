#include <iostream>

class A {
  public:
  virtual void print() {
    std::cout << "A\n";
  }
  int a_data;
};

class B : public A {
  public:
  virtual void print() {
    std::cout << "B\n";
  }
  int b_data;
};

class C : public B {
  public:
  virtual void print() {
    std::cout << "C\n";
  }
  int c_data;
};

void indirect(A *a) {
  a->print();
};

void direct_indirect(A &a) {
  (&a)->print();
}

int main() {

  A *a_ptr = new A;
  B *b_ptr = new B;
  C *c_ptr = new C;

  a_ptr = c_ptr;
  A a = *c_ptr;
  B *b = static_cast<B*>(&a);
  indirect(b);
  indirect(a_ptr);
}