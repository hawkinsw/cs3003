
class Addition(object):
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def __repr__(self):
    return "Addition"

class Subtraction(object):
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def __repr__(self):
    return "Subtraction"

class Multiplication(object):
  def __init__(self, left, right):
    self.left = left
    self.right = right
  def __repr__(self):
    return "Multiplication"

def exec(operation):
  if isinstance(operation, Addition):
    return operation.left + operation.right
  elif isinstance(operation, Subtraction):
    return operation.left - operation.right
    pass
  else:
    raise SyntaxError(f"exec cannot handle an {operation}.")

if __name__=='__main__':
  add = Addition(5, 4)
  subtract = Subtraction(5, 4)
  multiply = Multiplication(5, 4)
  print(f"exec(add): {exec(add)}")
  print(f"exec(subtract): {exec(subtract)}")
  print(f"exec(multiply): {exec(multiply)}")

