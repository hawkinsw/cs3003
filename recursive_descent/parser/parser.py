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
  def __init__(self, term, exprp):
    self.term = term
    self.exprp = exprp
  def __repr__(self):
    return f"Expr -> {self.term}{self.exprp}"

class ExprP(GoodNode):
  def __init__(self, term, exprp):
    self.term = term
    self.exprp = exprp
  def __repr__(self):
    return f"ExprP -> +{self.term}{self.exprp}"

class Term(GoodNode):
  def __init__(self, factor, termp):
    self.factor = factor
    self.termp = termp
  def __repr__(self):
    return f"Term -> {self.factor}{self.termp}"

class TermP(GoodNode):
  def __init__(self, factor, termp):
    self.factor = factor
    self.termp = termp
  def __repr__(self):
    return f"TermP -> *{self.factor}{self.termp}"

class Factor(GoodNode):
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
    if type(term) == BadNode:
      return BadNode(term.bad_token)

    exprp = self.parseExprP()
    if type(exprp) == BadNode:
      return BadNode(exprp.bad_token)

    return Expr(term, exprp)

  def parseExprP(self):
    tkn = self.nextToken()
    match tkn:
      case token.AddOperator():
        term = self.parseTerm()
        exprp = self.parseExprP()
        return ExprP(term, exprp)
      case _:
        self.pushbackToken(tkn)
        return Epsilon()

  def parseTerm(self):
    factor = self.parseFactor()
    termp = self.parseTermP()
    return Term(factor, termp)

  def parseTermP(self):
    tkn = self.nextToken()
    match tkn:
      case token.MultiplyOperator():
        factor = self.parseFactor()
        termp = self.parseTermP()
        return TermP(factor, termp)
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
