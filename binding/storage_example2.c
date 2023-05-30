#include <stdio.h>

//Which category does the localVar and result variables fall under?
//Is the address printed for localVar different from the address for the result variable? Why? 
int f1() {
    int localVar = 42;
    printf("Value of local var in f1 %d\n", localVar);
    printf("Address of local var in f1 %p\n", &localVar);
    return localVar;
}

int main() {
    int result = f1(); 
    printf("Value of local var in main %d\n", result);
    printf("Address of local var in main %p\n", &result);
    return 0;
}

