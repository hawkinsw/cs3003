def integer_square_root(x_squared: int) -> int:
  for i in range(x_squared):
    if i*i == x_squared:
      return i
    if i*i > x_squared:
      return -1
  return -1

def main():
  x_squared = 25
  x = integer_square_root(x_squared)
  if x >= 0:
    print(f"Square root of {x_squared} is {x}")
  else:
    print(f"Could not find an integer square root of {x_squared}")

if __name__=='__main__':
  main()
