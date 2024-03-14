#!/usr/bin/python3

if __name__ == "__main__":
    add_0 = __import__("add_0")

    a = 1
    b = 2

    result = add_0.add(a, b)
    print("{} + {} = {}".format(a, b, result))
