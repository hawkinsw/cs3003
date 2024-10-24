import ast
import pydot

class DotBuilder(ast.NodeVisitor):
  def __init__(self):
    # The keys in self.parents are ast.AST elements
    # and their values are a list of their children
    # ast.AST elements.
    self.parents = {}
    self.source_code = ""
    pass

  def make(self, node):
    self.source_code = f"{ast.unparse(node)}"
    self.visit(node)

  def visit(self, node):
    # NodeVisitor does _not_ provide any
    # default visit_Type methods, but will
    # try to call them if they exist in this
    # class. As long as we don't override
    # any of them, we will always end up at
    # generic_visit and that is where we can
    # do our work.
    super().visit(node)

  def generic_visit(self, parent):
    # First, add the node as a potential parent
    # into the list of parents.
    if parent not in self.parents:
      self.parents[parent] = []

    match parent:
      case ast.AST():
        for child_node in ast.iter_child_nodes(parent):
          match child_node:
            # Loads and Stores are uninteresting. So, let's leave them out.
            case ast.Load():
              pass
            case ast.Store():
              continue
            case _:
              # For everything that is not a Load/Store, it will be a
              # child of the parent.
              self.parents[parent].append(child_node)
              # And, recurse.
              self.visit(child_node)

  def finalize(self) -> pydot.Dot:
    graph = pydot.Dot()
    # All nodes in the graph, accessible by their corresponding ast.AST
    # object.
    graph_nodes = {}


    # Walk through all ast.ASTs in the parents ...
    for k in self.parents.keys():
      # Make a node in the graph for the parent if one does
      # not already exist.
      if k not in graph_nodes:
        graph_nodes[k] = pydot.Node(f"{k}")
        graph_nodes[k].set_label(f"{k.__class__.__name__}: {ast.unparse(k)}")
      parent_node = graph_nodes[k]
      graph.add_node(parent_node)

      # For each of the associated children of the parent, add an
      # edge in the graph. We may have to make a new node for the child
      # in the process.
      for child in self.parents[k]:
        if child not in graph_nodes:
          graph_nodes[child] = pydot.Node(f"{child}")
          graph_nodes[child].set_label(f"{child.__class__.__name__}: {ast.unparse(child)}")
        child_node = graph_nodes[child]
        graph.add_node(child_node)
        graph.add_edge(pydot.Edge(parent_node, child_node))

    graph.set_label(f"Derivation of Source Code: {self.source_code}")
    return graph

source_code = """
x = multiply(5, 2) + 2
"""

parsed = ast.parse(source_code)

dt = DotBuilder()
dt.make(parsed)

result = dt.finalize()
result.write_png("ast.png")