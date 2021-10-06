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

void use_a_destructable() {
  std::unique_ptr<Destructable> d = std::make_unique<Destructable>();
}

int main() {
  use_a_destructable();
  return 0;
}

