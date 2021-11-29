from .token import *

def tokenizer(input_file = None):
  if input_file == None:
    yield BadToken("No input file.", 0)
    return False

  with open(input_file) as file:
    file_contents = file.read()
    BEGIN = 0
    NUMBER = 1
    state = BEGIN
    lexeme = ""
    for i in range(len(file_contents)):
      if state == NUMBER:
        if file_contents[i].isdigit():
          # Continue accumulating the lexeme!
          lexeme += file_contents[i]
        else:
          # we are done with the lexeme!
          token = IntegerLiteral(int(lexeme))
          lexeme = ""
          state = BEGIN
          yield token
      if state == BEGIN:
        if file_contents[i] == '(':
          yield OpenParen()
        elif file_contents[i] == ')':
          yield CloseParen()
        elif file_contents[i] == '+':
          yield AddOperator()
        elif file_contents[i] == '*':
          yield MultiplyOperator()
        elif file_contents[i].isdigit():
          state = NUMBER
          lexeme += file_contents[i]
        elif not file_contents[i].isprintable() or \
             file_contents[i].isspace():
          pass
        else:
          yield BadToken(file_contents[i], i+1)
  while True:
    yield EOF()
