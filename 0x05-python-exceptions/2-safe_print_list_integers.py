#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            try:
                print(f"{my_list[i]:d}", end='')
                printed += 1
            except ValueError:
                pass
    except IndexError:
        pass

    print()
    return printed
