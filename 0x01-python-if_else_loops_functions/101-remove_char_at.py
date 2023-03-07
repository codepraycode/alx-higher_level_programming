#!/usr/bin/python3
def remove_char_at(string, n):
    new_str = ""
    for chi in range(len(string)):
        if chi != n:
            new_str += string[chi]
    return new_str
