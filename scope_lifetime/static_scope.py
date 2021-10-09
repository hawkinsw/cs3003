import inspect

def function_a():
    variable_v = "outer variable"
    def function_b():
        value_of_variable_v = variable_v
        print(f"variable_v: {value_of_variable_v}")

    def function_c():
      function_b()

    def function_d():
      variable_v = "not the outer variable."
      function_b()

    print("Calling function_c (BEGIN)")
    function_c()
    print("Calling function_c (END)")
    print("========================")
    print("Calling function_d (BEGIN)")
    function_d()
    print("Calling function_d (END)")

if __name__=="__main__":
  function_a()

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
