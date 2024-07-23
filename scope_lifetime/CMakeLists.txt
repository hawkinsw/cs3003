cmake_minimum_required(VERSION 3.25)

project(LifetimeAndScope DESCRIPTION "Demonstrate various lifetimes and scopes")

add_executable(Lifetime lifetime.cpp)
add_executable(ExplicitHeapDynamic explicit_heap_dynamic.cpp)
add_executable(Scope scope.cpp)
add_executable(ScopeArchive scope_archive.cpp)
if(${CMAKE_HOST_WIN32})
# Note: Make sure that you have enabled RelWithDebInfo (WIN32) for demo to work.
set_target_properties(Lifetime PROPERTIES COMPILE_OPTIONS "/W0" COMPILE_OPTIONS "/Od")
else()
set_target_properties(Lifetime PROPERTIES COMPILE_OPTIONS "-O0" COMPILE_OPTIONS "-g" COMPILE_OPTIONS "-Wno-return-stack-address")
endif()