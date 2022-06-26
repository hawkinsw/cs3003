#include <stdio.h>

struct count_up {
  int five;
  int six;
  int seven;
  int eight;
  int nine;
  int ten;
};

int square(struct count_up counter)
{
  printf("five: %d\n", counter.five);
  printf("six: %d\n", counter.six);
  printf("seven: %d\n", counter.seven);
  printf("eight: %d\n", counter.eight);
  return 0;
}
