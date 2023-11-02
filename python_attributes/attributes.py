
from typing import Any

class C:
    """ 
    A bit of playing around with __slots__ -- this will keep Python
    from creating a __dict__ for each of the instances of this class.
    """
    __slots__ = "member1", "member2"
    def __init__(self) -> None:
        self.member1 = "testing1"
        self.member2 = "testing2"

    def problem_causer(self):
        # This will cause a problem because we are using slots -- dynamically
        # adding attributes is not allowed in this case.
        try:
            self.oops = "This will cause a problem."
        except AttributeError as ae:
            print(f"Uhoh: {ae}")
            pass

class Descriptor:
    """
    A descriptor is something that Python knows how to use in order to
    provide programmatic power to set/get/delete attributes in a class.
    """
    def __init__(self): 
        pass
    def __get__(self, owner, ownertype=None):
        print(f"I am getting something for {id(owner)} and the owner has {ownertype=}.\n")

# Now, build a descriptor
# More on descriptors: https://docs.python.org/3/reference/datamodel.html#implementing-descriptors
getter = Descriptor()

class D:
    member1: str
    member2: str

    # By setting attr to getter as a class variable, then the
    # instance of Descriptor will be responsible for responding
    # when the user attempts to get/set/delete an attribute.
    descriptor_attr = getter
    def __init__(self) -> None:
        self.member1 = "testing1"
        self.member2 = "testing2"

    # Nothing but a traditional lookup!
    def found(self):
        print(f"Looking for found!")

    # __getattr__ will be invoked as a last-ditch effort to find
    # an attribute if it is not otherwise found.
    def __getattr__(self, attribute_name: str) -> Any:
        print(f"{attribute_name} is being sought. (through attr)")

    # __getattribute__ is unconditionally (!!) invoked and even seems
    # to prevent the access to getters even if it raises AttributeError.
    """
    def __getattribute__(self, attribute_name: str) -> Any:
        print(f"{attribute_name} is being sought (through getattribute).")
        raise AttributeError
    """

    def problem_causer(self):
        # This will *not* cause a problem because we are using slots -- dynamically
        # adding attributes is not allowed in this case.
        try:
            self.oops = "This will not cause a problem."
        except AttributeError as ae:
            print(f"We will not see this: {ae}")
            pass


def main():
    c = C()
    d = D()
    dd = D()

    print("About to cause a problem on class instance c.")
    c.problem_causer()
    print("About to (not) cause a problem on class instance d.")
    d.problem_causer()

    print("About to look for d.descriptor_attr.")
    print(f"{d.descriptor_attr=}")
    print("About to look for dd.descriptor_attr.")
    print(f"{dd.descriptor_attr=}")

    print("About to look for unfound.")
    d.unfound
    print("About to look for found.")
    d.found

if __name__ == '__main__':
    main()