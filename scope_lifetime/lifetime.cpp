#include <iostream>

bool *function1() {
  bool return_value = true;
  return &return_value;
}

int function2() {
  int return_value = 0;
  return return_value;
}

int main() {
	bool *function1_result = function1();
	int function2_result = function2();

	if (*function1_result) {
    std::cout << "True!\n";
	} else {
    std::cout << "False!\n";
  }
  return 0;
}
