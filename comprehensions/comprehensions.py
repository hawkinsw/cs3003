
def all_integers(low, high):
  return [x for x in range(low, high)]

def odd_integers(low, high):
  return [x for x in range(low, high) if x % 2]

def even_integers(low, high):
  return [x for x in range(low, high) if not (x % 2)]

def squares_of_integers(low, high):
  return [ x ** 2 for x in range(low, high)]

def verbose_squares_of_integers(low, high):
  return [ f"{x}**2={x**2}" for x in range(low, high)]

def split(lst):
  return lst[0], lst[1:]

def modern_split(lst):
  head, *tail = lst
  return head, tail

if __name__=='__main__':
  print(f"all_integers(5, 10): {all_integers(5, 10)}")
  print(f"odd_integers(5, 10): {odd_integers(5, 10)}")
  print(f"even_integers(5, 10): {even_integers(5, 10)}")
  print(f"squares_of_integers(5, 10): {squares_of_integers(5, 10)}")
  print(f"verbose_squares_of_integers(5, 10): {verbose_squares_of_integers(5, 10)}")

  lst = verbose_squares_of_integers(5,10)

  split_head, split_tail = split(lst)
  modern_head, modern_tail = modern_split(lst)

  print(f"split_head: {split_head}")
  print(f"split_tail: {split_tail}")
  print(f"modern_head: {modern_head}")
  print(f"modern_tail: {modern_tail}")
