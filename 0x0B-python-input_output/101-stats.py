#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
"""
import sys


def pretty_print(size, code_dict):
    """Pretty print data(dict)"""

    print("File size: {}".format(size))
    _data = sorted(code_dict.items())

    for key, value in _data:

        if (value != 0):
            print("{}: {}".format(key, value))

if __name__ == "__main__":
    """Script entry point to print the parsed data"""
    size = 0
    code_map = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        counter = 0

        for line in sys.stdin:
            
            counter += 1
            splitted_lines = line.split()

            code = splitted_lines[7]
            size += int(splitted_lines[8])

            if code in code_map:
                code_map[code] += 1

            if (counter % 10 == 0):
                pretty_print(size, code_map)

        pretty_print(size, code_map)
    except KeyboardInterrupt:
        pretty_print(size, code_map)
        raise
