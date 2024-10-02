cmake_minimum_required(VERSION 3.20)

project(Flake DESCRIPTION "The eBay for Cards")

add_executable(flake flake.cpp)
set_target_properties(flake PROPERTIES CXX_STANDARD 20)
target_include_directories(flake PUBLIC include)
