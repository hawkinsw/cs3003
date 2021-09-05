import inspect

def function_outer():
    outer_variable = "outer variable"
    def function_very_inner():
        value_of_outer_variable = outer_variable
        print(f"outer_variable: {value_of_outer_variable}")

    def function_inner_first():
      function_very_inner()

    def function_inner_second():
      outer_variable = "not the outer variable."
      function_very_inner()

    function_inner_first()
    function_inner_second()

if __name__=="__main__":
  function_outer()

"""
    Expected output:
    $ python3 './static_scope.py'
    outer_variable: outer variable
    outer_variable: outer variable
"""
