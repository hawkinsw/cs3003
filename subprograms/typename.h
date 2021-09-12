#ifndef __TYPENAME__H 
#define __TYPENAME__H 

#include <iostream>

template <typename T>
std::string type_name(T v) {
  return "Oops: cannot determine type!";
}

template <>
std::string type_name(int) {
  return "Integer";
}

template <>
std::string type_name(double) {
  return "Double";
}

template <>
std::string type_name(std::string) {
  return "String";
}

#endif
