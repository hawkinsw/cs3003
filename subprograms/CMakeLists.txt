cmake_minimum_required(VERSION 3.10)

project(Subprograms VERSION 1.0 DESCRIPTION "Subprograms")

add_executable(subprograms subprograms.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 17)

add_executable(coroutine coroutine.cpp)
set_property(TARGET subprograms PROPERTY CXX_STANDARD 20)

add_executable(simple_call simple_call.cpp)
set_property(TARGET simple_call PROPERTY CXX_STANDARD 20)