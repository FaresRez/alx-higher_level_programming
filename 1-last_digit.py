#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if (number < 0):
    a *= -1
if (a == 0):
    print("Last digit of", number, "is", a, "and is 0")
elif (a >= 6):
    print("Last digit of", number, "is", a, "and is greater than 5")
elif (a < 6):
    print("Last digit of", number, "is", a, "and is less than 6 and not 0")
