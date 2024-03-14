#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    total_number_of_args = len(sys.argv)
    result = 0

    sys.argv.pop(0)
    for item in sys.argv:
        result += int(item)

    print("{:d}".format(result))
