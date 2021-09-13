import time
import threading
import types

list_length = 500000000

def big_list(start, stop):
  i = start
  while i<stop:
    yield i
    i += 1

def take(amt, lst):
  """ Return the first _amt_ elements of _lst_ """
  taken = []
  i = 0
  if type(lst) == type([]):
    while i<amt:
      taken.append(lst[i])
      i += 1
  elif type(lst) == types.GeneratorType:
    while i<amt:
      taken.append(next(lst))
      i += 1
  return taken

def print_list(lst):
  """ Print the elements of _lst_ """
  for i in lst:
    print(f"{i}")
 
if __name__=='__main__':
  clk_id = time.pthread_getcpuclockid(threading.get_ident())

  print("Running the first version: ")

  before = time.clock_gettime_ns(clk_id)
  lst = [x for x in range(1,list_length)]
  print_list(take(50, lst))
  after = time.clock_gettime_ns(clk_id)
  print(f"First version took {(after-before)/1e9}s")

  print("Done printing. Probably starting a GC.")
  lst = []
  print("Done reseting. Probably done doing  a GC.")

  print("Running the second version: ")
  before = time.clock_gettime_ns(clk_id)
  snd_lst = big_list(1,list_length)
  print_list(take(50, snd_lst))
  after = time.clock_gettime_ns(clk_id)
  print(f"Second version took {(after-before)/1e9}s")
