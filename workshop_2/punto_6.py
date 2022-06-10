#!/usr/bin/python3

"""
Given two lists, a program must be created that generates a third list with the elements that are repeated in the two previous lists without repeating any element in the new list.
"""

list_1 = ['h', 'e', 'l', 'l', 'o', ' ', 't', 'e', 'a', 'm']
list_2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# Loop
new_list = []
for i in list_2:
    if i not in new_list and i in list_1:
        new_list.append(i)

# most efficient method - SETS
#new_list = list(set(list_1) & set(list_2))
print(new_list)
