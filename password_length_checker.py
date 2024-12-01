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




