#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_no_of_args = len(sys.argv)

    if total_no_of_args == 1:
        print("{:d} arguments.".format(0))
    elif total_no_of_args == 2:
        print("{:d} argument:".format(1))
    else:
        print("{:d} arguments:".format(total_no_of_args - 1))

    for i in range(1, total_no_of_args):
        print("{:d}: {}".format(i, sys.argv[i]))
