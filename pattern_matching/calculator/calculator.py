from decimal import DivisionByZero
from abc import abstractmethod

class Evaluatable():
  pass

class Constant(Evaluatable):
  def __init__(self, value: int) -> None:
    self.value = value

class BinaryOperator(Evaluatable):
  def __init__(self, left: Evaluatable, right: Evaluatable):
    self.left = left
    self.right = right
  @abstractmethod
  def __repr__(self):
    pass

class Addition(BinaryOperator):
  def __init__(self, left: Evaluatable, right: Evaluatable):
    super().__init__(left, right)
  def __repr__(self):
    return "Addition"

class Subtraction(BinaryOperator):
  def __init__(self, left: Evaluatable, right: Evaluatable):
    super().__init__(left, right)
  def __repr__(self):
    return "Subtraction"

class Multiplication(BinaryOperator):
  def __init__(self, left: Evaluatable, right: Evaluatable):
    super().__init__(left, right)
  def __repr__(self):
    return "Multiplication"

class Division(BinaryOperator):
  def __init__(self, left: Evaluatable, right: Evaluatable):
    super().__init__(left, right)
  def __repr__(self):
    return "Division"

def evaluate(operation) -> int:
  match operation:
    case Constant(value = f_value):
      return f_value
    case Addition(left = f_left, right = f_right):
      eleft = evaluate(f_left)
      eright = evaluate(f_right)
      return eleft + eright

    case Subtraction(left = f_left, right = f_right):
      eleft = evaluate(f_left)
      eright = evaluate(f_right)
      return eleft - eright

    case Division(left = f_left, right = f_right):
      eleft = evaluate(f_left)
      eright = evaluate(f_right)

      if (eright == 0):
        raise DivisionByZero()
      return eleft // eright

    case _: 
      raise SyntaxError(f"evaluate cannot handle a {operation}")

def demo() -> None:
  add = Addition(Constant(5), Constant(4))
  subtract = Subtraction(Constant(5), Constant(4))
  divide = Division(Addition(Constant(10), Constant(2)), Constant(4))
  multiply = Multiplication(Constant(5), Constant(4))
  print(f"exec(add): {evaluate(add)}")
  print(f"exec(subtract): {evaluate(subtract)}")
  print(f"exec(divide): {evaluate(divide)}")
  print(f"exec(multiply): {evaluate(multiply)}")
