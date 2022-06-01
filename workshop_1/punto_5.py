#!/usr/bin/python3

"""
From the previous exercise, create a program to calculate the final grade of a university student. To do this, the user must enter 3 grades and the percentage value of each grade, performs and returns the average on the screen.
"""

note1 = float(input(f"Please enter note 1: "))
percentage1 = int(input(f"Please enter percentage: "))
note2 = float(input(f"Please enter note 2: "))
percentage2 = int(input(f"Please enter percentage: "))
note3 = float(input(f"Please enter note 3: "))
percentage3 = int(input(f"Please enter percentage: "))

f1 = (note1 * percentage1) / 100
f2 = (note2 * percentage2) / 100
f3 = (note3 * percentage3) / 100

total_f = f1 + f2 + f3
total_p = percentage1 + percentage2 + percentage3
res = total_f / total_p
print(res)
