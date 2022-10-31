from typing import TextIO
import os

def generate_base(size: int, f: TextIO) -> None:
    tab = "\t"
    f.write(f"class Base{size} {{\n")
    for i in range(size):
        prefix = tab * 1
        method = f"{prefix}void m{i}() {{\n"
        method += f"{prefix}{tab}///\n"
        method += f"{prefix}}}\n"
        f.write(method)
    f.write(f"}}\n")
    return None

def generate_derived(base: str, size: int, f: TextIO) -> None:
    tab = "\t"
    f.write(f"class Derived{size} extends {base}{{\n")
    for i in range(size):
        prefix = tab * 1
        method = f"{prefix}void m{i}() {{\n"
        method += f"{prefix}{tab}///\n"
        method += f"{prefix}}}\n"
        f.write(method)
    f.write(f"}}\n")
    return None

def generate_main(size: int, f: TextIO) -> None:
    tab = "\t"
    f.write(f"public class Demo {{\n")
    f.write(f"{tab}public static void main(String args[]) {{\n")
    for i in range(size):
        f.write(f"{tab}{tab}Derived{i} d{i} = new Derived{i}();\n")
    f.write(f"{tab}}}\n")
    f.write(f"}}")

if __name__=="__main__":
    # First, let's create a folder for our .java file
    try:
        os.mkdir("java")
    except FileExistsError as fee:
        pass

    with open("java/Demo.java", 'w+') as f:
        generate_base(100, f)
        for i in range(100):
            generate_derived(f"Base100", i, f)
        generate_main(100, f)
    pass