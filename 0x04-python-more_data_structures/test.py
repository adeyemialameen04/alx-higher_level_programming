import random


def mul(num):
    return num * 2


def do_math(func, num):
    return func(num)


# print("8 * 2 =", do_math(mul, 8))


def get_func_mult_by_num(num):
    def mul_by(value):
        return num * value

    return mul_by


generated_func = get_func_mult_by_num(5)

# print("5 * 10 = ", generated_func(10))


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
# print(a_dictionary)

random_list = []

for i in range(1, 101):
    random_list += random.choice(['H', 'T'])

def gen_num_h_t(random_list):
    num_h = 0
    num_t = 0
    for i in random_list:
        if i == "H":
            num_h += 1
        elif i == "T":
            num_t += 1
    print(f"Head: {num_h}")
    print(f"Tail: {num_t}")


# gen_num_h_t(random_list)


oneTo10 = []

for i in range(1, 11):
    oneTo10.append(i)

def dbl_num(num):
    return num * 2


print(list(map(dbl_num, oneTo10)))
