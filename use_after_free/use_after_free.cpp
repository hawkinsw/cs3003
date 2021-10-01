#include <cstdint>
#include <iostream>
#include <string.h>

class Safe {
  public:
  virtual void safe_shutdown() {
    std::cout << "Safe shutdown\n";
  }
  virtual void safe_startup() {
    std::cout << "Safe startup\n";
  }
};

class Supervisor {
  public:
  virtual void supervisor_method() {
    std::cout << "Only supervisors can perform this operation\n";
  }
};

alignas(Safe) unsigned char buffer[sizeof(Safe)] = {};

template <typename T>
T *alloc() {
  return new(buffer) T;
}

void dealloc(void*) {
  memset(buffer, 0, sizeof(buffer));
}

bool is_supervisor() {
  return false;
}

int main() {
  Safe *a = alloc<Safe>();
  a->safe_startup();
  dealloc(a);

  Supervisor *b = alloc<Supervisor>();
  if (is_supervisor()) {
    /* We never do this operation because we are not a supervisor! */
    b->supervisor_method();
  }

  a->safe_shutdown();

}