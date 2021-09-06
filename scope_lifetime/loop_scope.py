def f():
  for i in range(1, 10):
    print(f"i (in loop body): {i}")
  print(f"i (outside loop body): {i}")

f()

"""
    expected output:
    $ python3 loop_scope.py
    i (in loop body): 1
    i (in loop body): 2
    i (in loop body): 3
    i (in loop body): 4
    i (in loop body): 5
    i (in loop body): 6
    i (in loop body): 7
    i (in loop body): 8
    i (in loop body): 9
    i (outside loop body): 9
"""
