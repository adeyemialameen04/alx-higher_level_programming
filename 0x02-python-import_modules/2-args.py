#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_no_of_args = len(sys.argv)

    if total_no_of_args == 1:
        print("0 arguments.")
    elif total_no_of_args == 2:
        print("1 argument:")
    else:
        print(f"{total_no_of_args - 1} arguments:")

    for i in range(1, total_no_of_args):
        print(f"{i}: {sys.argv[i]}")
