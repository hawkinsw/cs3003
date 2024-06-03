import inspect


def real_locals(lcls):
    """ real_locals: Find the actual locals of a function.
    
    The built - in function `locals` returns a mash up
    of the *actual *local variables and the free variables
    used by the local function rather than purely the
    locals (by definition of
    https://docs.python.org/3/reference/executionmodel.html#naming-and-binding).
    That's okay -- we can just subtract out the freevars
    and we'll end up with the right answer!
    """
    return lcls.keys() - \
        inspect.currentframe().f_back.f_code.co_freevars


def a():
    last_name = "Clapton"
    first_name = "Eric"
    print(f"{id(last_name)=}")
    print(f"{id(first_name)=}")

    def c():
        last_name = "Mayer"
        print(f"{real_locals(locals())=}")
        print(f"{locals()=}")
        print(f"{id(last_name)=} <-- Should differ from above.")
        # This statement will bring first_name in as a free variable.
        # See https://docs.python.org/3/reference/executionmodel.html#binding-of-names
        # Notice that it is in locals(). But, according to
        # the definition in the Python documentation, should it be?
        print(f"{id(first_name)=} <-- Should be the same as above.")
    c()

if __name__ == '__main__':
    a()
