#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments: ")

    sys.argv.pop(0)
    k = 0
    for i in sys.argv:
        print(f"{k + 1}: {i}")
        k += 1
