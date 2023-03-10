#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, each in enumerate(row):
            print("{:d}".format(each), end=" " if index != len(row)-1 else "\n")
