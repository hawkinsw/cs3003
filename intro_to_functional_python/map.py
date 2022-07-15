from operator import mul
from functools import partial

def my_partial(f, *l):
    def partially_evaluated_f(*x, **kwargs):
        return f(*l,*x, **kwargs)
    return partially_evaluated_f

if __name__=="__main__":
    myl = [x for x in range(0,9)]

    # map(f, l)
    # The `map` builtin function will invoke `f``, a function (really, a `Callable`),
    # one time for every element, `e` in `l`` using `e` as its argument. Therefore,
    # `f`` must execute properly when called with a single argument. The value generated
    # by each function invocation is added to a new list which is the value of the `map`
    # function invocation itself.
    #
    # Our problem to solve is that we are given a list of values (`myl`) and want to generate a
    # new list (`myll`) whose contents are the same values as the ones contained in `myl`,
    # just doubled.
    #
    # `mul` is a builtin function that will multiply two numbers. We could solve our problem
    # with
    
    myll = []
    for l in myl:
        myll.append(mul(2, l)) 
    
    # Is there a solution that uses `mul`? `mul` takes two parameters so it's not immediately
    # obvious whether it can be used in a call to `map`.
    #
    # To the rescue comes the `partial` function from the `functools` package. The `partial`
    # function takes a function, `z`, and a list `l`. It generates *a new function* whose 
    # parameters are the ones "unmatched" after assigning values to `z`'s parameters from 
    # the "arguments" given by the contents of `l`.
    # For example:

    def a_function_that_takes_three_parameters(a, b, c):
        """ This function does something with the parameters a, b and c. """
        pass
    a_function_that_takes_two_parameters = partial(a_function_that_takes_three_parameters, "some value for the a parameter")

    # A call to `a_function_that_takes_two_parameters` with the arguments 7, 8 -- ie, 
    a_function_that_takes_two_parameters(7, 8)
    # -- is identical to
    a_function_that_takes_three_parameters("some value for the a parameter", 7, 8)

    # Cool! That means that we can convert `mul` to a function that takes one parameter
    # because we know that we always invoke `mul` with the value 2 as the first argument
    # in the algorithm that solves our problem.
    mul2 = partial(mul, 2)
    # Feel free to take a look at the implementation (above) for `my_partial` for one
    # possible way of implementing `partial`. You can see the real version of the `partial`
    # implementation online at
    # https://github.com/python/cpython/blob/df4d53a09ab9fd9116d1b52bdc42133e019ca82b/Lib/functools.py#L276

    # And now we use `mul2` in `map` to create `myll`:
    myll = map(mul2, myl)
    print(list(myll))