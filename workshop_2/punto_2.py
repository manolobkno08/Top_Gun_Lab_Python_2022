#!/usr/bin/python3

"""
Given the two vehicle distances obtained and the time,
Given the two vehicle distances obtained and the time,
calculate whether you must pay a fine according to the following table.
calculate whether you must pay a fine according to the following table.

From 1 to 20 - Attention call for low speed.
speed.

From 21 to 60 - Normal

From 61 to 80 - Attention call for high speed.

From 81 to 120 - type tax 1

Over 120 - type tax 2 and immobilization of the vehicle.
"""

import os

run = True

while run:
    print("""
    WELCOME TO SPEED CAMERA

    Example of use:

    meters 1: 20.5
    meters 2: 20.5
    velocity in sec: 1.458

    Final velocity: 105 km/h

    """)
    distance_1 = float(input("Please enter the distance 1 in meters: "))
    distance_2 = float(input("Please enter the distance 2 in meters: "))
    time = float(input("Please enter the time in seconds: "))

    #f = (distance_1 + distance_2) / 2
    f = distance_1 + distance_2

    # Convert distance to km and time to hours.
    km = f / 1000.0
    time_hours = time / 3600.0

    # Calculate the final velocity
    velocity = km // time_hours
    print(f"Final velocity: {round(velocity)} km/h")

    flag = False

    # Check penalty type
    if velocity >= 1 and velocity <= 20:
        print("Attention call for low speed.")
    elif velocity >= 21 and velocity <= 60:
        print("Normal velocity.")
    elif velocity >= 61 and velocity <= 80:
        print("Attention call for hight speed.")
    elif velocity >= 81 and velocity <= 120:
        flag = True
        print("Penalty type 1")
    elif velocity > 120:
        flag = True
        print("Penalty type 2")

    # Check ethanola amount in blood
    if flag:
        ethanol = int(input("Enter amount of ethanol (mg): "))

        if ethanol >= 20 and ethanol <= 39:
            print(
                "Suspension of the driver's license between six (6) and twelve (12) months.")
        elif ethanol >= 40 and ethanol <= 99:
            print(
                """
First degree of drunkenness:

- Suspension of the Driver's License between one (1) and three (3) years.""")
        elif ethanol >= 100 and ethanol <= 149:
            print(
                """
Second degree of drunkenness:

- Suspension of Driver's License between three (3) and five (5) years.
- Take an awareness course of at least forty (40) hours.
                """
            )
        elif ethanol >= 150:
            print(
                """
Third degree of drunkenness:

- Suspension of Driver's License between three (5) and five (10) years.
- Take an awareness course of at least forty (80) hours.
                """
            )

    # Check if user wants to continue
    cont = str(input("\n¿Would you like to continue? y/n: "))
    if cont == "y":
        os.system("clear")
        pass
    else:
        print("See you soon!")
        break
