#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbers_printed = 0
    for e in range(x):
        try:
            print("{:d}".format(my_list[e]), end="")
            numbers_printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return numbers_printed
