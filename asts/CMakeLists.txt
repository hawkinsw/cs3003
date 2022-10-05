cmake_minimum_required(VERSION 3.10)

project(AST VERSION 1.0 DESCRIPTION "Show what a simple AST looks like")
include_directories("include/")
add_executable(ast ast.cpp)
