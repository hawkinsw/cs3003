cmake_minimum_required(VERSION 3.10)

project(Prototypes VERSION 1.0 DESCRIPTION "The importance of function prototypes and UB.")
set(PROJECT_SOURCES 
  definition.c
  user.c)

set(ALL_TARGETS 
  Prototype
  PrototypeOpt
  PrototypeUB
  PrototypeUBOpt)

set(UB_TARGETS
  PrototypeUB
  PrototypeUBOpt)

set(DB_TARGETS
  Prototype
  PrototypeOpt)

set(OPT_TARGETS
  PrototypeOpt
  PrototypeUBOpt)

add_executable(Prototype ${PROJECT_SOURCES})
add_executable(PrototypeOpt ${PROJECT_SOURCES})
add_executable(PrototypeUB ${PROJECT_SOURCES})
add_executable(PrototypeUBOpt ${PROJECT_SOURCES})

foreach(target ${DB_TARGETS})
  target_compile_options(${target} PUBLIC -DUB=0)
endforeach()

foreach(target ${UB_TARGETS})
  target_compile_options(${target} PUBLIC -DUB=1)
endforeach()

foreach(target ${OPT_TARGETS})
  target_compile_options(${target} PUBLIC -O3)
endforeach()

foreach(target ${ALL_TARGETS})
  target_compile_options(${target} PUBLIC -g)
endforeach()
