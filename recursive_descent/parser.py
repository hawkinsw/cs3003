from lexer import tokenizer, token
from parser import parser

tknzr = tokenizer.tokenizer("testing.input")
#tknzr = tokenizer.tokenizer()

parser = parser.Parser(tknzr)

print(parser.parseExpr())
