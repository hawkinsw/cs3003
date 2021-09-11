""" Examples of writing list comprehensions in Python. """

def all_integers(low, high):
  """ Generate a list of all the integers between low and high. """
  return [x for x in range(low, high)]

def odd_integers(low, high):
  """ Generate a list of all odd integers between low and high. """
  return [x for x in range(low, high) if x % 2]

def even_integers(low, high):
  """ Generate a list of all even integers between low and high. """
  return [x for x in range(low, high) if not (x % 2)]

def squares_of_integers(low, high):
  """ Generate a list of the squares of all integers between low and high. """
  return [ x ** 2 for x in range(low, high)]

def verbose_squares_of_integers(low, high):
  """ Generate a list of equations for the squares of all integers between low and high. """
  return [ f"{x}**2={x**2}" for x in range(low, high)]

if __name__=='__main__':
  print(f"all_integers(5, 10): {all_integers(5, 10)}")
  print(f"odd_integers(5, 10): {odd_integers(5, 10)}")
  print(f"even_integers(5, 10): {even_integers(5, 10)}")
  print(f"squares_of_integers(5, 10): {squares_of_integers(5, 10)}")
  print(f"verbose_squares_of_integers(5, 10): {verbose_squares_of_integers(5, 10)}")
