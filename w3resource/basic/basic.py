#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
Exercises basic, from w3resources.

'''

'''
28. Write a Python program to print all even numbers from a given 
    numbers list in the same order and stop the printing if any numbers 
    that come after 237 in the sequence.

'''
def print_even_numbers():
    numbers = [    
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
        953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
        626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,
        379, 843, 831, 445, 742, 717, 958,743, 527
        ]

    for n in numbers:
        if n == 237:
            break
        elif n % 2 == 0:            
            print(n)


'''
30. Write a Python program that will accept the base and height of a
    triangle and compute the area.

'''
def calc_area_triangle(base, height):
    area = base * height / 2
    print('Triangle area:', area)


'''
45. Write a python program to call an external command in Python.
'''
from subprocess import call

def call_external_command(command_):
    # 'o argumento deve ser uma lista.'
    # call(['ls', '-l'])
    call(command_)


'''    
48. Write a Python program to parse a string to Float or Integer.
'''
def parse_to_float(string_):
    print(float(string_), type(float(string_)))
    print(int(string_) ,type(int(string_)))
  

'''
51. Write a Python program to determine profiling of Python programs.
    Note: A profile is a set of statistics that describes how often and 
    for how long various parts of the program executed. These statistics 
    can be formatted into reports via the pstats module.     

'''


def print_profile():
    for i in range(1000):
        print(i * 3 / 4)


'''
64. Write a Python program to get file creation and modification
    date/times.

'''


def get_file_infos(file_):
    pass


'''
96. Write a Python program to print the current call stack.

'''

def print_curr_stack():
    pass


'''
101. Write a Python program to access and print a URL's content to the
    console.
'''
from http.client import HTTPConnection


def print_content_url(url_):
    conn = HTTPConnection('example.com')
    conn.request('GET', '/')
    result = conn.getresponse()
    contents = result.read()
    print(contents.decode('ascii'))

'''
109. Write a Python program to check if a number is positive, negative 
    or zero.
'''
def check_number(number):
    if number == 0:
        print('Number is 0.')
    elif number < 0:
        print('Number is negative.')
    else:
        print('Number is positive')


'''
131. Write a Python program to split a variable length string into 
    variables.

'''
def split_string(string_):
    list_ = []
    for i in string_.split(' '):
        list_.append(i)

    print(list_)


if __name__ == "__main__":
    print_content_url('https://docs.python.org/3/library/http.server.html')