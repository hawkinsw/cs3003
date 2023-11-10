#include <iostream>
#include <memory>

class Destructable {
  public:
  Destructable() {
    std::cout << "I am destructable.\n";
  }

  ~Destructable() {
    std::cout << "I am a destructable that is being destructed!\n";
  }
};

void unique_use_a_destructable() {
  std::cout << "unique_use_a_destructable()\n";
  std::unique_ptr<Destructable> d = std::make_unique<Destructable>();
  // When d goes out of scope, there is absolutely no other potential
  // referrent to the memory, so we should destroy it!
}

void shared_use_a_destructable() {
  std::cout << "shared_use_a_destructable()\n";
  std::shared_ptr<Destructable> d = std::make_shared<Destructable>();
  {
    // We will create a copy of that shared pointer and 
    // assign it to another shared pointer. This action
    // will increase the use count by 1.
    std::shared_ptr<Destructable> a{d};
    std::cout << "Use count? " << a.use_count() << "\n";
    // When the shared pointer a goes out of scope, then
    // the use count will drop by 1.
  }
  std::cout << "Use count? " << d.use_count() << "\n";
  // When the last reference to the shared memory goes out of
  // scope, then we can delete it!
}

void memory_leak() {
  Destructable *d{new Destructable{}};
}
void no_memory_leak() {
  // Notice how there is not much additional programmer
  // overhead needed to get the benefit of guaranteed
  // memory reclamation.
  std::unique_ptr<Destructable> d{new Destructable{}};
}

int main() {
  unique_use_a_destructable();
  shared_use_a_destructable();
  memory_leak();
  no_memory_leak();
  return 0;
}

