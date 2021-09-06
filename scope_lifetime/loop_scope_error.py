def f():
  print(f"i (outside loop body): {i}")
  for i in range(1, 10):
    print(f"i (in loop body): {i}")

f()

"""
    expected output:
    $ python3 loop_scope_error.py
    Traceback (most recent call last):
      File "loop_scope_error.py", line 6, in <module>
        f()
      File "loop_scope_error.py", line 2, in f
        print(f"i (outside loop body): {i}")
    UnboundLocalError: local variable 'i' referenced before assignment
""" 
