#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        res = i
        if (i % 3 == 0) and (i % 5 == 0):
            res = "FizzBuzz"
        elif i % 3 == 0:
            res = "Fizz"
        elif i % 5 == 0:
            res = "Buzz"
        print(res, end=" ")
