#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for e in my_list[:x]:
        print(e, end="")
    print()