#!/usr/bin/python3

"""
The method was called Jumping to 5. It is a simple and ingenious strategy, each digit is changed to the opposite digit of the telephone keypad by jumping to the number 5, as shown in the following figure:

As shown in the figure:-from 1 it jumps to 9 and from 9 to 1 (above 5).-from 2 it jumps to 8 and from 8 to 2 (above 5).-from 3 it jumps to 7 and from 7 to 3 (above 5).-from 4 it jumps to 6 and from 6 to 4 (above 5).-from 5 it jumps to 0 and from 0 to 5.Thus when a message was passed first all the numbers in it were encoded according to the jumps.

For example, if the message is: "Call after 9:54 to phone 3122345676", the coded message would be: "Call after 1:06 to phone 7988760434".

"""
from data_dec import data


def coded_decode(message: str) -> str:
    """ Function get string to coded and decoded message """
    message = list(message)
    for i in range(0, len(message)):
        for key, value in data.items():
            if message[i] == key:
                message[i] = value
                break
    return ''.join(message)


if __name__ == '__main__':
    try:
        menu = int(input("""
Hi, please choose one of the following:

1. Coded
2. Decoded

: """))

        if menu == 1:
            message = str(input("\nPlease, enter the message to encoded: "))
        elif menu == 2:
            message = str(input("\nPlease, enter the message to decoded: "))
        else:
            pass
        res: str = coded_decode(message)
        print("\nMessage encoded: " + res if menu ==
              1 else "\nMessage decoded: " + res)
    except ValueError:
        print("Incorrect value")
    except NameError:
        print("Incorrect value")

    # Examples
    # message = "Call after 9:54 to phone 3122345676"
    # message2 = "Call after 1:06 to phone 7988760434"
