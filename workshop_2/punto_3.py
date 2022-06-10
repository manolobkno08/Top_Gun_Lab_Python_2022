#!/usr/bin/python3

"""
Without resistance bodies fall at the same velocity regardless of their mass, shape and composition. When an object is dropped, the distance it travels is proportional to the time d = v∗t ± (12)∗g∗𝑡2, where

- d is the distance traveled.
- g is the acceleration originated by gravity, i.e., 9.8𝑚𝑠2.
- t is the elapsed time.

In honor of the great scientist Galilei, it would be necessary to implement an application that, given the height in meters of a building from which a sphere is to be launched, would show the distance traveled second by second until it hits the ground.
"""

height_meters = float(input(f"Please enter the height in meters: "))
metters_count = 0
iter = 1

while metters_count <= height_meters:
    metters_count = (((1/2) * 9.8) * (iter**2))
    print(
        f"Distance traveled per second {iter}: {round(metters_count, 2)} meters")
    iter += 1
