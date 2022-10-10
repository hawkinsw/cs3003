from lexer import tokenizer
from lexer import token

class Node(object):
  pass

class BadNode(Node):
  def __init__(self, bad_token):
    self.bad_token = bad_token
  def __repr__(self):
    return f"Parse error: {self.bad_token}"
  pass

class GoodNode(Node):
  pass

class Expr(GoodNode):
  def __init__(self, term, expr):
    self.term = term
    self.expr = expr
  def __repr__(self):
    return f"Expr -> {self.term}{self.expr}"

class ExprPrime(GoodNode):
  def __init__(self, term, expr_prime):
    self.term = term
    self.expr_prime = expr_prime
  def __repr__(self):
    return f"ExprPrime -> +{self.term}{self.expr_prime}"

class Term(GoodNode):
  def __init__(self, factor, term):
    self.factor = factor
    self.term = term
  def __repr__(self):
    return f"Term -> {self.factor}{self.term}"

class TermPrime(GoodNode):
  def __init__(self, factor, term_prime):
    self.factor = factor
    self.term_prime = term_prime
  def __repr__(self):
    return f"TermPrime -> *{self.factor}{self.term_prime}"

class Factor(GoodNode):
  # This is basically just eating it because we are only 
  # concerned about what comes nested inside it.
  pass

class Id(GoodNode):
  def __init__(self, token):
    self.token = token
  def __repr__(self):
    return f"Id: {self.token}"

class Epsilon(GoodNode):
  def __repr__(self):
    return "Epsilon"

class Parser(object):
  def __init__(self, tokenizer):
    self.tokenizer = tokenizer
    self.redo_tkn = None

  def pushbackToken(self, token):
    self.redo_tkn = token

  def nextToken(self):
    if self.redo_tkn:
      tkn = self.redo_tkn
      self.redo_tkn = None
      return tkn
    else:
      return next(self.tokenizer)

  def parseExpr(self):
    term = self.parseTerm()
    match term:
      case BadNode():
        return BadNode(term.bad_token)
    exprp = self.parseExprPrime()
    match exprp:
      case BadNode():
        return BadNode(exprp.bad_token)
    return Expr(term, exprp)

  def parseExprPrime(self):
    tkn = self.nextToken()
    match tkn:
      case token.AddOperator():
        term = self.parseTerm()
        exprp = self.parseExprPrime()
        return ExprPrime(term, exprp)
      case _:
        self.pushbackToken(tkn)
        return Epsilon()

  def parseTerm(self):
    factor = self.parseFactor()
    termp = self.parseTermPrime()
    return Term(factor, termp)

  def parseTermPrime(self):
    tkn = self.nextToken()
    match tkn:
      case token.MultiplyOperator():
        factor = self.parseFactor()
        termp = self.parseTermPrime()
        return TermPrime(factor, termp)
      case _:
        self.pushbackToken(tkn)
        return Epsilon()

  def parseFactor(self):
    tkn = self.nextToken()
    match tkn:
      case token.OpenParen():
        expr = self.parseExpr()
        tkn = self.nextToken()
        if type(tkn) != token.CloseParen:
          return BadNode(tkn)
        else:
          return expr
      case token.IntegerLiteral(value=value):
        return Id(value)
