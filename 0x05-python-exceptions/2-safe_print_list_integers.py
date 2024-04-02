#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print(f"{my_list[i]:d}", end='')
            printed += 1
    except (IndexError, TypeError, ValueError):
        pass

    print()
    return printed
