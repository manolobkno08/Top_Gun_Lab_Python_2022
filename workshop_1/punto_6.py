#!/usr/bin/python3

"""
The following matrix (or list with nested lists)
must fulfill that the fourth element of each row is
the sum of the first three elements of the respective row.
If you notice that the sums you find are wrong, you must
modify them by giving 2 solutions, one with append and
one with slicing.
"""

matriz = [[2, 4, 3, 6], [8, 3, 4, 5], [7, 1, 3, 10], [9, 2, 1, 4]]

# Slicing solution ----------
matriz[0][-1] = sum(matriz[0][:3])
matriz[1][-1] = sum(matriz[1][:3])
matriz[2][-1] = sum(matriz[2][:3])
matriz[3][-1] = sum(matriz[3][:3])
print(matriz)

# Append solution ------------
matriz[0].pop(3)
matriz[0].append(sum(matriz[0]))

matriz[1].pop(3)
matriz[1].append(sum(matriz[1]))

matriz[2].pop(3)
matriz[2].append(sum(matriz[2]))

matriz[3].pop(3)
matriz[3].append(sum(matriz[3]))
print(matriz)
