#!/usr/bin/python3
def print_last_digit(number):
    n = int(str(number)[-1])
    if (n < 0):
        n *= -1
    print(n, end="")
    return n
