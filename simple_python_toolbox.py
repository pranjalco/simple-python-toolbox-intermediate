# Importing all functions from functions module.
from functions import *
from art import logo

"""
# Project: Simple Python Toolbox Version 2
# Description: 
This is my first project, which I have updated after enhancing my skills. The program serves as a versatile toolbox to 
perform everyday tasks such as:

    - Checking the length of a password
    - Performing basic calculations with a simple calculator
    - Counting words in a given sentence
    - Converting temperatures between Celsius and Fahrenheit

The program provides an interactive menu where users can select the task they want to perform, and it delivers results 
based on their choice. This toolbox is designed to simplify small yet common tasks in a single, user-friendly 
application.

# Level: Intermediate
Author: Pranjal Sarnaik
Date: 2024-12-01
"""

# Starting Program and welcome greeting
border = ('-' * 40)

print(border)
print("Welcome to the Simple Python Toolbox")
print(f"{border}\n")

# Asking user to enter their name and age
name = input("Please enter your name:\n")
age = input("Please enter your age:\n")
# print(f"Hello {name}! your age is {age}")
print(f"\n{border}\n")

while True:

    print(f"Hello {name} welcome to:")
    print(logo)
    # Asking user to choose a task to do
    task = (input("""Please tell us what task you wanted to do, type short form of task.
    1. Password Length Checker: PLC
    2. Simple Calculator: SC
    3. Word Counter: WC
    4. Temperature Converter: TC
    
    Choose 'Q' to quit the program.
    """)).upper()
    print(f"You choose {task}")
    print(f"\n{border}\n")

    if task == 'Q':
        break

    if task == 'PLC':
        password_length_checker()

    elif task == 'SC':
        calculator()

    elif task == 'WC':
        word_counter()

    elif task == 'TC':
        temperature_converter()

    else:
        print("Please enter valid input ('PLC', 'SC', 'WC', 'TC')")
        print(f"\n{border}\n")
        continue

print("End of the program.")
print(f"Hello {name}, Thanks for using Simple Python Toolbox!")
