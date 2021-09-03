import inspect

def show_referencing_environment():
  frame = inspect.currentframe()
  frame = frame.f_back
  print("Contents of the referencing environment:")
  print("\n".join(frame.f_locals.keys()))


def testing():
  five = 5
  pass

def outer_function(parameter_one = None, parameter_two = None):
  outer_local1 = None
  def inner_function(inner_parameter_one = None, inner_parameter_two = None):
    if outer_local1 == None:
      pass
    if outer_local2 == None:
      pass
    inner_local1 = None
    inner_local2 = None
    def inner_inner_function():
      nonlocal outer_local1
      nonlocal outer_local2

      nonlocal five

      if inner_local1 == None:
        pass
      if inner_local2 == None:
        pass
      inner_inner_local1 = None
      inner_inner_local2 = None
      show_referencing_environment()
    inner_inner_function()

  outer_local2 = None
  inner_function()

if __name__=='__main__':
  outer_function()
