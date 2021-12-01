from .token import *

class FAState(object):
  pass
class BEGIN(FAState):
  pass
class NUMBER(FAState):
  pass

def in_state(actual, expected):
  return type(actual) == expected

def new_state(new_state):
  return new_state()

def tokenizer(input_file = None):
  if input_file == None:
    yield BadToken("No input file.", 0)
    return False

  with open(input_file) as file:
    file_contents = file.read()
    state = new_state(BEGIN)
    buf = ""
    for i in range(len(file_contents)):
      if in_state(state,NUMBER):
        if file_contents[i].isdigit():
          buf += file_contents[i]
        else:
          intlex = int(buf)
          token = IntegerLiteral(intlex)
          buf = ""
          state = new_state(BEGIN)
          yield token
      # Careful: This is *not* an elsif intentionally. If
      # we saw a non-digit when we were in the NUMBER state,
      # we changed state to the BEGIN state, yielded a
      # IntegerLiteral token ... BUT still need to handle
      # the character that bumped us out of the NUMBER state.
      # This is a shortcut, but one that I think is okay!
      if in_state(state,BEGIN):
        if file_contents[i] == '(':
          yield OpenParen()
        elif file_contents[i] == ')':
          yield CloseParen()
        elif file_contents[i] == '+':
          yield AddOperator()
        elif file_contents[i] == '*':
          yield MultiplyOperator()
        elif file_contents[i].isdigit():
          state = new_state(NUMBER)
          buf = file_contents[i]
        elif not file_contents[i].isprintable() or \
             file_contents[i].isspace():
          pass
        else:
          yield BadToken(file_contents[i], i+1)
  while True:
    yield EOF()
