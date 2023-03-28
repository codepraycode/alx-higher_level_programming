#!/usr/bin/python
def safe_print_list(my_list=[], x=0):
    try:
        number_of_real_elements = 0
        for e in my_list[:x]:
            number_of_real_elements += 1
            print(e, end="")
        print()
    except Exception:
        pass
    return number_of_real_elements

