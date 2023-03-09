#!/usr/bin/python3
def uppercase(text):
    for e in text:
        char = ord(e)
        if char >= 97 and char <= 97+25:
            char -= 32
        print("{}".format(chr(char)), end="")
    print()
