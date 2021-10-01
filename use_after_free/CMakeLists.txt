cmake_minimum_required(VERSION 3.10)

project(UseAfterFree VERSION 1.0 DESCRIPTION "UseAfterFree")

add_compile_options(-Wall -Wextra -pedantic -Werror)
add_executable(use_after_free use_after_free.cpp)
