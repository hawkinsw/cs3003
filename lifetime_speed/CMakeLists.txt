cmake_minimum_required(VERSION 3.10)

project(LifetimeSpeed VERSION 1.0 DESCRIPTION "Does lifetime affect speed.")
include_directories("include/")
# These options are necessary for the demo to succeed. Why? Because without
# them both static_ and local functions contain indirect memory accesses.
add_executable(LifetimeSpeed main.cpp)
target_compile_options(LifetimeSpeed PUBLIC -fno-pic -fno-PIC -fno-pie -static)
target_link_options(LifetimeSpeed PUBLIC -static)

add_executable(LifetimeSpeedSlow main.cpp)