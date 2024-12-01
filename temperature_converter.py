def temperature_converter():
    """This function takes temperature in celsius and return it by converting it in fahrenheit."""

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


temperature_converter()
