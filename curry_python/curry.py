#!/usr/bin/env python

def sum3(a, b, c):
  return a + b + c

def sum1(a):
  def sum2(b):
    def sum3(c):
      return a + b + c
    return sum3
  return sum2


if __name__=='__main__':
  print(f"sum3(1, 2, 3): {sum3(1, 2, 3)}");
  sum3(1, 2, 3)
  print(f"sum1(1)(2)(3): {sum1(1)(2)(3)}");
  sum1(1)(2)(3)
