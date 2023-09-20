

def num_maker():
    for i in range(1000):
        yield i

def main():
    counter = 0
    for i in num_maker():
        counter = counter + 1
        print(f"{i=}")
    print(f"{counter=}")
main()