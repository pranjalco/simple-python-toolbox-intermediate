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
            print("ZeroDivisionError: Devision by zero is not possible please select value other than 0")
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
            r = add(num1, num2)

        elif operation == "S":
            o = "Subtraction"
            r = sub(num1, num2)

        elif operation == "M":
            o = "Multiplication"
            r = mul(num1, num2)

        elif operation == "D":
            o = "Division"
            r = div(num1, num2)

        else:
            print("Please choose valid input opeartion ('A', 'S', 'M', 'D')")
            continue  # Restarting loop when user enter invalid input

        if r is not None:
            print(f"The result of {o} is {r}\n")

    print("End of calculator program!")
    print(f"\n{border}\n")

calculator()