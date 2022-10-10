from abc import abstractmethod
from dataclasses import dataclass
from typing import ClassVar, Optional, Union
from typing_extensions import Self
from lexer import token
from treelib import Tree, Node as TreeNode

@dataclass
class Node(object):
  __nodeIDCounter: ClassVar[int] = 0

  nodeID: str

  def __init__(self):
    self.nodeID = str(Node.__nodeIDCounter)
    Node.__nodeIDCounter += 1

  @abstractmethod
  def tree_node(self, tree: Tree, parent: Optional[TreeNode]):
    pass

  def __getattr__(self, attribute: str):
    if attribute == "node_repr":
      return self.__repr__()
    else:
      raise AttributeError()

class BadNode(Node):
  def __init__(self, bad_token):
    super().__init__()
    self.bad_token = bad_token
  def __repr__(self):
    return f"Parse error: {self.bad_token}"
  def tree_node(self, tree: Tree) -> TreeNode:
    return tree.create_node(self.nodeID, self.nodeID, data=self)
  pass

class GoodNode(Node):
  def __init__(self):
    super().__init__()
  pass

class Id(GoodNode):
  def __init__(self, token):
    super().__init__()
    self.token = token
  def __repr__(self):
    return f"Id: {self.token}"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    return this_node

class Expr(GoodNode):
  def __init__(self, term, expr):
    super().__init__()
    self.term = term
    self.expr = expr
  def __repr__(self):
    return f"Expr"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    self.term.tree_node(tree, this_node)
    self.expr.tree_node(tree, this_node)
    return this_node

class ExprPrime(GoodNode):
  def __init__(self, term, expr_prime):
    super().__init__()
    self.term = term
    self.expr_prime = expr_prime
  def __repr__(self):
    return f"ExprPrime"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    self.term.tree_node(tree, this_node)
    self.expr_prime.tree_node(tree, this_node)
    return this_node

class Term(GoodNode):
  def __init__(self, factor, term):
    super().__init__()
    self.factor = factor
    self.term = term
  def __repr__(self):
    return f"Term"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    self.term.tree_node(tree, this_node)
    self.factor.tree_node(tree, this_node)
    return this_node

class Factor(GoodNode):
  id: Optional[Id]
  expr: Optional[Expr]

  # This is basically just eating it because we are only 
  # concerned about what comes nested inside it.
  def __init__(self, wrapped: Union[Id, Expr]):
    super().__init__()
    self.id = None
    self.expr = None
    match wrapped:
      case Id(_):
        self.id = wrapped
      case Expr():
        self.expr = wrapped
      case _:
        raise AssertionError()

  def __repr__(self):
    if self.id != None:
      return f"Factor of Id: {self.id}"
    return f"Factor of (Expr): {self.expr}"

  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    if self.id != None:
      self.id.tree_node(tree, this_node)
    elif self.expr != None:
      self.expr.tree_node(tree, this_node)
    return this_node
  pass


class TermPrime(GoodNode):
  factor: Factor
  term_prime: Self
  def __init__(self, factor, term_prime):
    super().__init__()
    self.factor = factor
    self.term_prime = term_prime
  def __repr__(self):
    return f"TermPrime"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    self.term_prime.tree_node(tree, this_node)
    self.factor.tree_node(tree, this_node)
    return this_node

class Epsilon(GoodNode):
  def __init__(self):
    super().__init__()
  def __repr__(self):
    return "Epsilon"
  def tree_node(self, tree: Tree, parent: TreeNode) -> TreeNode:
    this_node: TreeNode = tree.create_node(self.nodeID, self.nodeID, data=self, parent=parent)
    return this_node

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
        if type(expr) == BadNode:
          return BadNode(tkn)
        tkn = self.nextToken()
        if type(tkn) != token.CloseParen:
          return BadNode(tkn)
        else:
          return Factor(expr)
      case token.IntegerLiteral(value=value):
        return Factor(Id(value))

  def tree_at(self, node: Node, result: Tree = Tree()):
    node.tree_node(result, None)
    return result
