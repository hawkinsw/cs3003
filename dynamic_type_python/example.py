from bintrees import BinaryTree

class Address():
    def __init__(self, street: str):
        self.__street = street

    def move_in(self, company):
        print(f"Congratulations on your new home at {self.__street};")
        print(f"I hope that {company} moves your belongings without breaking them!")

if __name__ == "__main__":
    pine = Address("349 Pine Dr.")
    print(f"{type(pine)=}")

    pine.move_in("Sure Hands")

    pine = BinaryTree()
    print(f"{type(pine)=}")

    pine.move_in("Sure Hands")

