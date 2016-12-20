'''
Program: Calculator
Author: Joel Thomas Guros
Copyright: 2016
Description: a basic calculator written in Python 3.5.2.
'''

import re

print("My calculator.")
print("Type 'quit' to exit\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""

    # If there has been a previous calculation, use that as the prompt.
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # If user quits ->
    if equation == 'quit':
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
