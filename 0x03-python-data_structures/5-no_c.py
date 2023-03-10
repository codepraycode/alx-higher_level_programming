#!/usr/bin/python3
def no_c(my_string):
    return "".join([e if e.lower() != 'c' else '' for e in my_string])