"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here

while 1:
    input_string = input()
    tokened_input = input_string.split(" ")

    if "q" in tokened_input:
        print("Bye!")
        break

    elif len(tokened_input) < 2:
        print("Try again!")
        continue

    operator = tokened_input[0]
    num1 = float(tokened_input[1])

    if len(tokened_input) < 3:
        num2 = 0

    else:
        num2 = float(tokened_input[2])

    if len(tokened_input) > 3:
        num3 = float(tokened_input[3])

    if tokened_input[0] == "q":
        quit()
    elif tokened_input[0] == "+":
        print(add(num1, num2))
    elif tokened_input[0] == "-":
        print(subtract(num1, num2))
    elif tokened_input[0] == "*":
        print(multiply(num1, num2))
    elif tokened_input[0] == "/":
        print(divide(num1, num2))
    elif tokened_input[0] == "square":
        print(square(num1))
    elif tokened_input[0] == "cube":
        print(cube(num1))
    elif tokened_input[0] == "pow":
        print(power(num1, num2))
    elif tokened_input[0] == "mod":
        print(mod(num1, num2))
    elif tokened_input[0] == "x+":
        print(add_mult(num1, num2, num3))
    elif tokened_input[0] == "cubes+":
        print(add_cubes(num1, num2))
    else:
        print("try again")
