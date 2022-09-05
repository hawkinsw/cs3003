cmake_minimum_required(VERSION 3.10)

project(LifetimeSpeed VERSION 1.0 DESCRIPTION "Does lifetime affect speed.")
include_directories("include/")
# These options are necessary for the demo to succeed. Why? Because without
# them both static_ and local functions contain indirect memory accesses.
add_compile_options(-fno-pic -fno-PIC -fno-pie -static)
add_link_options(-static)
add_executable(LifetimeSpeed main.cpp)
