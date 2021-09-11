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
    def inner_inner_function(parameter1 = None):
      nonlocal outer_local1
      nonlocal outer_local2

      # Uncommenting this line will break the program? Why?
      # Because only variables that are in lexical scope
      # can be brought in to this scope using the nonlocal
      # keyword. five is in the lexical scope of testing
      # but not either inner_function nor outer_function.
      # https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement
      #nonlocal five

      if inner_local1 == None:
        pass
      if inner_local2 == None:
        pass
      inner_inner_local1 = None
      inner_inner_local2 = None

      # The locals function will print out the referencing environment
      # of the statement. In other words, it will print out all the 
      # identifiers that can be used to access variables at this point
      # in the program.
      print(f"locals: {locals()}")

    inner_inner_function()

  outer_local2 = None
  inner_function()

if __name__=='__main__':
  outer_function()
