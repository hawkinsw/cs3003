import inspect

def function_blue():
    variable_v = "outer variable"
    def function_pink():
        value_of_variable_v = variable_v
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
    $ python3 ./static_scope.py
    Calling function_c (BEGIN)
    variable_v: outer variable
    Calling function_c (END)
    ========================
    Calling function_d (BEGIN)
    variable_v: outer variable
    Calling function_d (END)
"""
