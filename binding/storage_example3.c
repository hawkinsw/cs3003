#include <stdio.h>
#include <stdlib.h>

//Which category does the localVar variable fall under?
//What does the malloc and free operation do?
//What happens if you free first and then print?
void f1() {
    int* localVar = (int*)malloc(sizeof(int));
    *localVar = 42;
    printf("Value of local var %d\n", *localVar);
    free(localVar);
}

int main() {
    f1();
    return 0;
}

