#!/usr/bin/python3
import random
number = random.randint(-10, 10)
valueType = "zero"
if number > 0:
    valueType = "positive"
elif number < 0:
    valueType = "negative"

print(f"{number} is {valueType}")
