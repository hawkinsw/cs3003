import inspect

def dynamic(lexical_variable_value, variable_name):
    value = lexical_variable_value
    # We start at the 2nd index because
    # 0: this function (dynamic)
    # 1: the function calling this (which includes a local
    #    variable named _variable_name_.
    # 2: the function that called (1) and is the first
    #    place where a meaningful reassignment could be.
    for containing_frame, _, _, _, _, _ in inspect.stack()[2:]:
        try:
            value = containing_frame.f_locals[variable_name]
            break
        except KeyError:
            pass
        finally:
            del containing_frame
    return value

def function_outer():
    outer_variable = "outer variable"
    def function_very_inner():
        value_of_outer_variable = dynamic(outer_variable, "outer_variable")
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
    $ python3 ./dynamic_scope.py
    outer_variable: outer variable
    outer_variable: not the outer variable.
"""
