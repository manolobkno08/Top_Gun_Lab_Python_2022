#!/usr/bin/python3

"""
You must use everything you know about strings,
lists and their methods or functions to transform
the following text:
"""

my_str = "    thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado… -agrega el comentarista"

wo_char = my_str.replace('#', ' ')

my_list = wo_char.split()

new_str = ""
new_str += my_list[0].capitalize() + ' '
new_str += ' '.join(my_list[1:4]) + '...\n'
new_str += '- ¡' + my_list[4].capitalize() + ' '
new_str += ' '.join(my_list[5:13]) + '.\n'
new_str += '-  ' + my_list[13].capitalize() + ' ' + my_list[14]
new_str += ' ' + my_list[15][1:] + ' '
new_str += ' '.join(my_list[16:18]) + '.\n'
new_str += '-  ' + my_list[18].capitalize() + ' '
new_str += ' '.join(my_list[19:24]) + ' '
new_str += ' '.join(my_list[24:]) + '.'

print(new_str)
