cmake_minimum_required(VERSION 3.10)

project(Subprograms VERSION 1.0 DESCRIPTION "Subprograms")

add_executable(subprograms subprograms.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 17)

add_executable(coroutine coroutine.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 20)

add_executable(simple_call simple_call.cpp)
set_property(TARGET simple_call PROPERTY CXX_STANDARD 20)
target_compile_options(simple_call PUBLIC -g -O0)
add_custom_target(Objdump ALL DEPENDS "${CMAKE_SOURCE_DIR}/simple_call.obj")
add_custom_command(OUTPUT "${CMAKE_SOURCE_DIR}/simple_call.obj" DEPENDS simple_call COMMAND objdump -D -Mintel "$<TARGET_FILE:simple_call>" > "${CMAKE_SOURCE_DIR}/simple_call.obj")
