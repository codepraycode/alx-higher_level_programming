#!/usr/bin/python3

def extract_value(tuple_, index):

    try:
        return tuple_a[index]
    except IndexError:
        return 0

def add_tuple(tuple_a=(), tuple_b=()):

    val1 = extract_value(tuple_a, 0)
    val2 = extract_value(tuple_a, 1)
    
    val11 = extract_value(tuple_b, 0)
    val22 = extract_value(tuple_b, 1)

    return (val1 + val11, val2 + val22)