#!/bin/env python

import gc, sys

class MakeItMineMetaclass(object):
  def __new__(cls, classname, bases, attrs):
    my_attrs = { "My" + key: value for key, value in attrs.items()}
    return type(classname, bases, my_attrs)
  pass

class MyClass(metaclass=MakeItMineMetaclass):
  a = 1
  b = 2

class ClassWithEmptyString:
  def __init__(self):
    self.empty = ""

def referrers():
  stringa = ClassWithEmptyString()
  stringb = ClassWithEmptyString()

  referrers = gc.get_referrers("")

  print(f"id(stringa) = {id(stringa)}")
  print(f"id(stringb) = {id(stringb)}")
  print(f"id(locals()['stringa']) = {id(locals()['stringa'])}")
  print("sys.getrefcount(\"\") = " + str(sys.getrefcount("")))
  print("sys.getrefcount(\"\") = " + str(sys.getrefcount("")))

  if id(stringa) in [id(x) for x in referrers] and id(stringb) in [id(x) for x in referrers]:
    print(f"Yes, both stringa and stringb *do* refer to the empty string.")
  else:
    print(f"Yes, one of stringa and stringb *does no* refer to the empty string.")

  """
  for referrer in referrers:
    lcls = locals()
    glbls = globals()
    v = [id(x) for x in gc.get_referents(referrer)]
    print(f"{v=}")
    # v = [gc.get_referents(name) for name in lcls.keys() if lcls[name] is referrer]
    # print(f"{v=}")
    # v = [gc.get_referents(name) for name in glbls.keys() if glbls[name] is referrer]
    # print(f"{v=}")
  """


def play():
  type_of_string = type("")
  type_of_string_dict = type_of_string.__dict__
  keys_values = list(zip(type_of_string_dict.keys(), type_of_string_dict.values()))

  for key, value in  keys_values:
    print(f"{key=} {value=}")

if __name__=="__main__":
  referrers()
  mc = MyClass()
  print(f"{mc.__getattribute__('Myb')}")
