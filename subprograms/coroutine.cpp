#include <iostream>

int num_maker() {
    int static last_number = 0;
    if (last_number<1000)
        return last_number++;
    return -1;
}

int main() {
    int counter{0};
    for (int i = num_maker(); i != -1; i = num_maker()) {
        counter = counter + 1;
        std::cout << "i=" << i << std::endl;
    }
    std::cout << "counter=" << counter << std::endl;
    return -1;
}