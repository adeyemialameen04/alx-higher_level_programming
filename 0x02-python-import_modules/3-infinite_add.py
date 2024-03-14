#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    total_number_of_args = len(sys.argv)
    result = 0

    for i in range(1, total_number_of_args):
        result = int(sys.argv[i]) + result


    print("{:d}".format(result))