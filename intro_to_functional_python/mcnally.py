from operator import mul
from typing import Callable, List, TypeVar
from numbers import Number


def mk_func_to_multiply_by(scale: Number) -> Callable[[Number], Number]:
    def func_that_multiplies_by(operand: Number) -> Number:
        return mul(scale, operand)
    return func_that_multiplies_by


InputListElementType = TypeVar('InputListElementType')
OutputListElementType = TypeVar('OutputListElementType')


def mcnally(list: List[InputListElementType],
            one_arg_function: Callable[[InputListElementType], OutputListElementType]) -> List[OutputListElementType]:
    result = []
    for l in list:
        result.append(one_arg_function(l))
    return result


if __name__ == "__main__":

    """ We could 
        1. go through each element in a list and
           a. apply a function to that element
           b. append the result to another list
        and we would get a new list whose values are
        based on the original list in some way.
    """

    # For instance, let's make each word in a list all uppercase.
    whisper = ["hello", "my", "name", "is", "audrey"]
    shout = []
    for quiet in whisper:
        shout.append(str.upper(quiet))
    assert(["HELLO", "MY", "NAME", "IS", "AUDREY"] == shout)

    # Or, let's calculate whether each work in a list is all uppercase.
    speech = ["You", "ARE", "doing", "GREAT"]
    is_shouted = []
    for word in speech:
        is_shouted.append(str.isupper(word))
    assert([False, True, False, True] == is_shouted)

    """ But, this type of pattern is very, very common. So, let's
        write a function that does the same thing. We call this function
        mcnally. It takes two parameters:
        1. A list to transform.
        2. A function that does the transformation; the function itself
           takes a single argument (the element to transform).
    """
    is_shouted = mcnally(speech, str.isupper)
    assert([False, True, False, True] == is_shouted)

    """ If we want to multiply each number in a list by two, we can
        almost apply the same pattern using the mul function. Too bad
        the mul function takes two parameters!
    """
    single = [1, 2, 3, 4]
    double = []
    for s in single:
        double.append(mul(2, s))
    assert([2, 4, 6, 8] == double)

    """ What if we had a function that converted functions with two
        parameters
        1. fixed the first of those parameters to a particular value and, thus, 
        2. returned a new function that took one parameter! 
        Then we could use this pattern!
    """
    multiply_by_2 = mk_func_to_multiply_by(2)
    assert(8 == multiply_by_2(4))
    multiply_by_5 = mk_func_to_multiply_by(5)
    assert(20 == multiply_by_5(4))

    # Voila
    single = [1, 2, 3, 4]
    double = mcnally(single, multiply_by_5)
    assert([5, 10, 15, 20] == double)
