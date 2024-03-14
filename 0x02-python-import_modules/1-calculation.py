#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calculator_var

    a = 10
    b = 5

    print("{} - {} = {}".format(a, b, calculator_var.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_var.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_var.div(a, b)))
