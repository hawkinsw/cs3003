cmake_minimum_required(VERSION 3.10)

project(Subprograms VERSION 1.0 DESCRIPTION "Subprograms")

add_executable(subprograms subprograms.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 17)

add_executable(coroutine coroutine.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 20)

add_executable(stack_frame stack_frame.c)
set_property(TARGET stack_frame PROPERTY C_STANDARD 17)
target_compile_options(stack_frame PUBLIC -g -O0 -m32)
target_link_options(stack_frame PUBLIC -g -O0 -m32)
add_custom_target(Objdump ALL DEPENDS "${CMAKE_SOURCE_DIR}/stack_frame.obj")
add_custom_command(OUTPUT "${CMAKE_SOURCE_DIR}/stack_frame.obj" DEPENDS stack_frame COMMAND objdump -D -Mintel "$<TARGET_FILE:stack_frame>" > "${CMAKE_SOURCE_DIR}/stack_frame.obj")
