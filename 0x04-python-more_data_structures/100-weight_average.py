#!/usr/bin/python3

def weight_average(my_list=[]):

    if not my_list:
        return 0

    sum_tuple = 0
    avg = 0
    for item in my_list:
        times = item[0] * item[1]
        sum_tuple += times
        avg += item[1]
    weight_avg = float(sum_tuple / avg)
    return weight_avg
