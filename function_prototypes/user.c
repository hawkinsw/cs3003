#include <stdio.h>

#if UB != 1
struct count_up {
  int five;
  int six;
  int seven;
  int eight;
  int nine;
  int ten;
};
extern int square(struct count_up);
#endif

int main() {
  int five = 5;
  int six = 6;
  int seven = 7;
  int eight = 8;
#if UB != 1
  struct count_up counter = {five, six, seven, eight};
  square(counter);
#else
  square();
#endif
}
