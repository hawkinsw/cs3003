cmake_minimum_required(VERSION 3.10)

project(StackFrameDemo VERSION 1.0 DESCRIPTION "A demo of stack frames!")
include_directories("include/")
add_executable(StackFrameDemo main.c)
# Add the following options to make the demo work:
# 1. -m32 Required so that we are allowed to use the cdecl calling
#    convention and get the parameters passed on the stack.
# 2. -fno-pic -fno-pie Required so that we don't get position-independent
#    code. PIC on 32-bit inserts a ton of "thunks" and really messes
#    up the code.
# 3. -O0 Don't optimize -- the compiler is too good.
# 4. -g Well, why not?
target_compile_options(StackFrameDemo PUBLIC -m32 -O0 -g -fno-pic -fno-pie)
target_link_options(StackFrameDemo PUBLIC -m32)
