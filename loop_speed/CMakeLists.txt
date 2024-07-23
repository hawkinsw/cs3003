cmake_minimum_required(VERSION 3.10)

project(LoopSpeed VERSION 1.0 DESCRIPTION "LoopSpeed")

#add_compile_options(-Wall -Wextra -pedantic -O3)
include_directories("include/")
add_executable(loop_speed loop_speed.cpp)
