
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

if __name__=='__main__':
  add = Addition(5, 4)
  subtract = Subtraction(5, 4)
  five = 5
  six = 6.0
  seven = "seven"

  if isinstance(add, Addition):
    print("add is an Addition object!")
  if isinstance(subtract, Subtraction):
    print("subtract is a Subtraction object!")
  if isinstance(five, int):
    print("five is an int!")
  if isinstance(six, float):
    print("six is a float!")
  if isinstance(seven, str):
    print("seven is a string!")
  if not isinstance(add, Subtraction):
    print("add is not a Subtraction object!")
