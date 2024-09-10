from typing import Callable
import timeit

def addition(i: int, j: int) -> int:
    return i + j


def single_addition(i: int)-> Callable[[int], int]:
    def local_addition(j: int) -> int:
        return i + j
    return local_addition

def time_single_addition(low: int, high: int) -> int:
    result: int = 0
    for i in range(low, high):
        result += single_addition(low)(i)

def time_single_addition_cached(low: int, high: int) -> int:
    result: int = 0
    saved = single_addition(low)
    for i in range(low, high):
        result += saved(i)

def time_addition(low: int, high: int) -> int:
    result: int = 0
    for i in range(low, high):
        result += addition(low,i)

def actually_time_addition() -> int:
    return time_addition(1, 100)

def actually_time_single_addition() -> int:
    return time_single_addition(1, 100)

def actually_time_single_addition_cached() -> int:
    return time_single_addition_cached(1, 100)

if __name__=="__main__":
    print(timeit.timeit("actually_time_single_addition()", setup="from __main__ import actually_time_single_addition"))
    print(timeit.timeit("actually_time_single_addition_cached()", setup="from __main__ import actually_time_single_addition_cached"))
    print(timeit.timeit("actually_time_addition()", setup="from __main__ import actually_time_addition"))
