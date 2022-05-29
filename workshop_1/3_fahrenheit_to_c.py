#!/usr/bin/python3

class Temp():
    """
    Temperature class representation
    """

    def __init__(self, value):
        """Initialize attributes"""
        self.value = value

    def fahrenheit_to_celsius(self):
        """Convert from fahrenheit to celsius"""
        return (self.value - 32) * (5/9)

    def celsius_to_fahrenheit(self):
        """Convert from celsius to fahrenheit"""
        return (self.value * (9/5)) + 32


if __name__ == '__main__':
    try:
        option = int(input("""
Please select one of the following options:

1. Convert Fahrenheit to Celsius
2. Convert Celsius to Fahrenheit

Your option: """))

        if option == 1:
            value = float(input("\nPlease enter temperature in Fahrenheit: "))
            f = Temp(value)
            res = f.fahrenheit_to_celsius()
            print(f"{round(res, 1)} C")
        elif option == 2:
            value = float(input("\nPlease enter temperature in Celsius: "))
            c = Temp(value)
            res = c.celsius_to_fahrenheit()
            print(f"{round(res, 1)} F")
        else:
            print("Option not valid")

    except ValueError:
        print("Your option must be numeric")