#include <stdio.h>

//How would you make the f1 function history sensitive?
//Which category does the counter variable fall under?
//If counter is stack dynamic, what is its scope and lifetime?
//If counter is static, what is its scope and lifetime?
void f1() {
    int counter = 0;
    counter++;
    printf("Invocation number: %d\n", counter);
}

int main() {
    f1();
    f1();
    f1();
    
    return 0;
}

