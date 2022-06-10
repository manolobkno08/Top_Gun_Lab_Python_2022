#!/usr/bin/python3

"""
A program must be created that, given a length in squares (greater than zero), generates a board
"""
length_squares = int(input(f"Please enter the length of the square: "))

for i in range(length_squares):
    for j in range(length_squares):
        if (i + j) % 2 != 0:
            print("#", end=' ')
        else:
            print(" ", end=' ')
    print('\n', end='')
