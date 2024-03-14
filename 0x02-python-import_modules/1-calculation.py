import calculator_1 as calculator_var

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator_var.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_var.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_var.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_var.div(a, b)))
