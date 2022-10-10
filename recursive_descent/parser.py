from lexer import tokenizer
from parser import parser

contents, tknzr = tokenizer.create_tokenizer("testing.input")

parser = parser.Parser(tknzr)
parsed = parser.parseExpr()

print(f"\n\n{contents=}\n...\nparses as ...\n")
tree = parser.tree_at(parsed)
tree.show(data_property="node_repr")