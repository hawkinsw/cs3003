from typing import Any, Callable, List, TypeVar

#
# The type annotation on `f` is to indicate that the function
# taken as a parameter must take only a single parameter (of any type)
# and needs to meet no criteria for the type of its return vaue.
T = TypeVar('T')
def foreach(f: Callable[[T], Any], list: List[T]) -> None:
    for item in list:
        f(item)

if __name__=="__main__":
    # A list comprehension (https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
    # used to fill a list with 0, 1, 2, 3
    myl = [x for x in range(0,4)]
    # The foreach function will apply the function given in the first parameter to each element in the 
    # list. There is a requirement that the function passed as parameter be able to operate when inoked
    # with a single argument (either because it only has 1 parameter *or* because the remaining parameters
    # have default values.)
    foreach(print, myl)