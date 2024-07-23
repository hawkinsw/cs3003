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

def function_blue():
    variable_v = "outer variable"
    def function_pink():
        value_of_variable_v = dynamic(variable_v, "variable_v")
        print(f"variable_v: {value_of_variable_v}")

    def function_green():
      function_pink()

    def function_yellow():
      variable_v = "not the outer variable."
      function_pink()

    print("Calling function_green (BEGIN)")
    function_green()
    print("Calling function_green (END)")
    print("========================")
    print("Calling function_yellow (BEGIN)")
    function_yellow()
    print("Calling function_yellow (END)")

if __name__=="__main__":
  function_blue()

"""
    Expected output:
    $ python3 ./dynamic_scope.py
    Calling function_green (BEGIN)
    variable_v: outer variable
    Calling function_green (END)
    ========================
    Calling function_yellow (BEGIN)
    variable_v: not the outer variable.
    Calling function_yellow (END)
"""
