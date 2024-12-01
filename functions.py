# This file contains all necessary functions used in Simple Python Utility project.

def word_counter():
    """This function takes sentence from user and splits it, and return the count of the number
    of words in the sentence."""

    border = ('-' * 40)

    # Taking sentence from user as input
    sentence = input("Please enter a sentence:\n")
    print(f"\n{border}\n")

    # Counting words in sentence by splitting the sentence by spaces
    word_count = len(sentence.split())

    # Checking if count is zero or not incase if user did not enter any input
    if word_count == 0:
        print("No words or sentence entered, so the count is 0.")
        print(f"\n{border}\n")
    else:
        print(f"Total count of words in your sentence is {word_count}")
        print(f"\n{border}\n")

    # Returning the final word count
    return word_count


def temperature_converter():
    """This function takes temperature in Celsius and return it by converting it in Fahrenheit."""

    border = ('-' * 40)

    while True:
        try:
            temperature_celsius = int(input("Enter temperature in celsius: "))
            break
        except ValueError:
            print("Error: Invalid input provided, \nPlease enter integer value.")
    fahrenheit = (temperature_celsius * (9 / 5)) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}°F")
    print(f"\n{border}\n")


def password_length_checker():

    """This function tells us the length of our password."""

    border = ('-' * 40)

    # Asking user to enter password
    password = input("Please enter password to check length\n")

    # Checking length of password
    length = len(password)

    # Printing final result
    print("The length of password is {}".format(length))
    print(f"\n{border}\n")


def calculator():
    """This is simple calculator function used to do Addition, Subtraction, multiplication and Division
    based on user input. It takes two numbers from user and then do the calculation."""

    # This is border variable which we will use to separate parts of program wherever necessary.
    border = ('-' * 40)

    # Defining functions to do calculation operations

    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2

    # Here in division we are checking the condition where the second number is zero,
    # and if it is zero then how to handle this condition.
    def div(num1, num2):
        if num2 == 0:
            print("ZeroDivisionError: Division by zero is not possible please select value other than 0")
            return None
        else:
            return num1 / num2

    # Here the loop will continue to run until the user choose to quit the program by pressing Q as input in operation.
    while True:

        # Asking user for two numbers to perform calculation and also ask them which operation they wanted to perform

        try:
            number1 = int(input("Please enter number one: "))
            number2 = int(input("Please enter number two: "))
        except ValueError:
            print("Invalid input! Please enter valid integers.")
            continue

        print(f"\n{border}\n")

        # Asking user to which operation to perform on a numbers
        operation = input("""Please tell us which operation you want to perform, choose short form of it.
        Addition: A 
        Subtraction: S
        Multiplication: M
        Division: D

        or press 'Q' to quit the program
        """).upper()
        print(f"You choose {operation}")
        print(f"\n{border}\n")

        if operation == 'Q':
            print("Thanks for using calculator! exiting now.")
            break  # Exiting the loop

        if operation == "A":
            o = "Addition"
            r = add(number1, number2)

        elif operation == "S":
            o = "Subtraction"
            r = sub(number1, number2)

        elif operation == "M":
            o = "Multiplication"
            r = mul(number1, number2)

        elif operation == "D":
            o = "Division"
            r = div(number1, number2)

        else:
            print("Please choose valid input operation ('A', 'S', 'M', 'D')")
            continue  # Restarting loop when user enter invalid input

        if r is not None:
            print(f"The result of {o} is {r}\n")

    print("End of calculator program!")
    print(f"\n{border}\n")
