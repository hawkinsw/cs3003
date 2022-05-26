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
    print(f"{id(last_name)=}")

    def c():
        last_name = "Mayer"
        print(f"{real_locals(locals())=}")
        print(f"{locals()=}")
        print(f"{id(last_name)=}")
        eval('print(f"{id(last_name)=}")')
    c()
    eval('print(f"{id(last_name)=}")')


if __name__ == '__main__':
    a()
