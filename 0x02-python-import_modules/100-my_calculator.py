#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    first_operand = int(sys.argv[1])
    second_operand = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print("{} + {} = {}".format(first_operand, second_operand, add(first_operand, second_operand)))
    elif operator == "-":
        print("{} - {} = {}".format(first_operand, second_operand, sub(first_operand, second_operand)))
    elif operator == "*":
        print("{} * {} = {}".format(first_operand, second_operand, mul(first_operand, second_operand)))
    elif operator == "/":
        print("{} / {} = {}".format(first_operand, second_operand, div(first_operand, second_operand)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

