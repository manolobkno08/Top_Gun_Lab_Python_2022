#!/usr/bin/python3

"""
The following graph shows the behavior of the descendants and ascendants of a person, if we assume that this person is generation 0, generation 1 will be two people (his parents) generation 2 will be 4 people (his grandparents) and so on.

You must create a program that given a generation (greater than or equal to zero):
- Tells the user the total number of people in the family (of all generations up to the given generation).
- Display the number of people in each generation while doing the calculation.
"""

gen = int(input(f"Please enter the generation: "))

if gen >= 0:
    i = 0
    j = 1
    while i <= gen:
        print(f"Gen {i} - people number: {j}")
        j *= 2
        i += 1
else:
    print("Input invalid")
