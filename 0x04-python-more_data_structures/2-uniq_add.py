#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniques = set(my_list)
    sum = 0

    for num in uniques:
        sum += num
    return sum
