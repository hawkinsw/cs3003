from lexer import tokenizer
from parser import parser

tknzr = tokenizer.tokenizer("testing.input")

parser = parser.Parser(tknzr)
parsed = parser.parseExpr()

print(parsed)