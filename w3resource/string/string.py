# -*- coding: utf-8 -*-

'''
Exercises string.

'''

'''
1. Write a Python program to calculate the length of a string   
'''


def calc_length_str(string):
    return len ( string )


'''
8. Write a Python function that takes a list of words and returns the length of the longest one.
'''


def get_the_longest(args):
    longest = 0
    index_longest = 0

    for i , arg in enumerate ( args ):
        if len ( arg ) > longest:
            longest = len ( arg )
            index_longest = i

    return args[index_longest]


'''
10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
'''


def change_first_last(string):
    return ''.join ( [string[-1] , string[1:-1] , string[0]] )


'''
11. Write a Python program to remove the characters which have odd index values of a given string.
'''


def remove_odd_index(string):
    new_string = ''

    for i in range ( len ( string ) ):
        if i % 2 == 0:
            new_string += string[i]

    return new_string


'''
17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
Sample function and result : 
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
'''


def change_str(string):
    return string[-2:] * 4


'''
28. Write a Python program to add a prefix text to all of the lines in a string.
'''


def add_prefix(string):
    return string.replace('\n','\n>')


'''
29. Write a Python program to set the indentation of the first line.
'''


# Corrigir
def set_indent(string):
    return ''.join ( ['\t' , string] )


'''
34. Write a Python program to print the following integers with '*' on the right of specified width.
'''


def print_format(value):
    return '{:*<4d}'.format ( value )


'''
47. Write a Python program to lowercase first n characters in a string.
'''


def lowercase_chars(string , n):
    return string[:n].lowercase + string[n:]


'''
48. Write a Python program to swap comma and dot in a string.
#Sample string: \"32.054,23\"
# Expected Output: \"32,054.23\"
'''


# Corrigir
def format_decimal(string):
    return string.replace ( ',' , '.' ).replace ( '.' , ',' , 1 )


if __name__ == "__main__":
    sample_text = '''
        Python is a widely used high-level, general-purpose, interpreted,
        dynamic programming language. Its design philosophy emphasizes
        code readability, and its syntax allows programmers to express
        concepts in fewer lines of code than possible in languages such
        as C++ or Java.
        '''
    print ( add_prefix ( sample_text ) )

