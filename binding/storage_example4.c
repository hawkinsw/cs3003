#include <stdio.h>
#include <stdlib.h>

//Which category does the localVar and result variables fall under?
//Is the address printed for localVar different from the address for the result variable? Why? 
//What happens if you call free() in f1, what happens if you call free() in main.
//Should you call free() in both functions?
//Experiment with the code and try to answer the above questions.
int* f1() {
    int* localVar = (int*)malloc(sizeof(int));
    *localVar = 42;
    printf("Value of local var in f1 %d\n", *localVar);
    printf("Address of local var in f1 %p\n", localVar);
    return localVar;
}

int main() {
    int* result = f1(); 
    printf("Value of local var in main %d\n", *result);
    printf("Address of local var in main %p\n", result);
    return 0;
}

