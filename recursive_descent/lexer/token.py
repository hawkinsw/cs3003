class Token:
  pass

class BadToken(Token):
  def __init__(self, lexeme, place):
    self.lexeme = lexeme
    self.place = place
  def __repr__(self):
    return f"Bad token ({self.lexeme}) at {self.place}"

class EOF(Token):
  def __repr__(self):
    return "EOF"

class ValidToken(Token):
  pass

class OpenParen(ValidToken):
  def __repr__(self):
    return "("

class CloseParen(ValidToken):
  def __repr__(self):
    return "CloseParen: )"

class AddOperator(ValidToken):
  def __repr__(self):
    return "+"

class MultiplyOperator(ValidToken):
  def __repr__(self):
    return "*"

class IntegerLiteral(ValidToken):
  def __repr__(self):
    return f"{self.value}"

  def __init__(self, value = 0):
    self.value = value
