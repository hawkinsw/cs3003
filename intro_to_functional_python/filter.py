
def is_even(x: int) -> bool:
    """ Return True if `x` is even; return False otherwise. """
    if x % 2 == 0:
        return True
    return False

if __name__=="__main__":
    myl = [x for x in range(0, 4)]

    # `filter` is a builtin function that takes two parameters (a function, `f`, and a list, `l`)
    # and returns a list. The list that `filter` returns contains all the elements `i` in `l` such
    # that `f(i)` is `True`.A
    #
    # The problem we are asked to solve is to turn a list of numbers (`myl`) into a new list (`myll`)
    # that contains *only* the values of `myll` that are even. We could easily solve that using a loop:

    myll = []
    for i in myl:
        if is_even(i):
            myll.append(i)

    # Could we solve it using `filter` somehow? Of course! In fact, the loop we just wrote is almost a
    # direct translation of the description of the `filter` function. So, let's solve it this way:
    myll = filter(is_even, myl)
    print(list(myll))

    # What if we did not have a function named `is_even`? Could we still use `filter`? Yes! We could 
    # use a `lambda` (https://docs.python.org/3/reference/expressions.html#lambda) which is a type of
    # function (really a `Callable`) without a name:
    myll = filter( lambda x: x % 2 == 0, myl)
    print(list(myll))