import time
import sys

def memory_usage():
    return sys.getallocatedblocks()

def use_space():
    return [x for x in range(1600000)]

class Sandwich:
    bread: [int]
    def __init__(self) -> None:
        print(f"Make me a sandwich, clown.")
        self.bread = use_space()

if __name__=="__main__":
    catering = []

    for i in range(2):
        print(f"Notice that there is minimal data used: {memory_usage()=}")
        print("Not quite ...")
        print(f"{sys.getsizeof(catering)}")
        time.sleep(5)

    for _ in range(10):
        # This is where the implicit heap dynamic happens.
        # Until this statement is executed, there is no space
        # allocated for the instance of Sandwich. Only when
        # we execute this statement is space allocated dynamically
        # on the heap to hold its values.
        tuna_on_toast = Sandwich()
        catering.append(tuna_on_toast)
        print(f"Notice that memory usage is starting to climb: {memory_usage()=}")
        time.sleep(1)

    while not len(catering) == 0:
        _ = catering.pop()
        # Here is another cool aspect of the "implicit" part
        # of implicit heap dynamic: When the memory is no
        # longer used, the language takes care of cleaning
        # it up for us!
        print(f"Notice that memory usage is starting to decline: {memory_usage()=}")
        time.sleep(1)
