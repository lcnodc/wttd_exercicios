#!/usr/bin/env python
#-*- coding: utf-8 -*-


'''
Exercises List: 21 29 30 31 33 38 39 43 44 59
'''


'''
21. Write a Python program to convert a list of characters into a string.
'''
def list_to_string(list_):

    return ''.join(map(str, list_))



'''
29. Write a Python program to get unique values from a list. 
'''
# Or using sets
def get_uniques(list_):
    # uniques = []
    #
    # for i in list_:
    #     if i not in uniques:
    #         uniques.append(i)
    #
    # return uniques
    return list(set(list_))


'''
30. Write a Python program to get the frequency of the elements in a list.
'''
import collections

def get_frequency(list_):
    # frequency = []
    #
    # for i in list_:
    #     if (i, list_.count(i)) not in frequency:
    #         frequency.append((i, list_.count(i)))
    #
    # return frequency
    return collections.Counter(list_)


''''
31. Write a Python program to count the number of elements in a list within a 
    specified range.
'''
def count_elements(list_, min, max):
    q = 0

    for i in list_:
        if i >= min and i <= max:
            q += 1

    return q


'''
33. Write a Python program to generate all sublists of a list.
'''
# Corrigir
def generate_sublist(list_):
    subs = [[]]

    for i in range(len(list_)):
        n = i + 1

        while n <= len(list_):
            sub = list_[i:n]
            subs.append(sub)
            n += 1

    return  subs

'''
38. Write a Python program to change the position of every n-th value with the
    (n+1)th in a list.
'''
# Corrigir
def change_position(list_):
    temp = 0
    value = 0

    for i, v in enumerate(list_):
        temp = list_[i + 1]


'''    
39. Write a Python program to convert a list of multiple integers into a 
    single integer. 
    
    Sample list: [11, 33, 50]
    Expected Output: 113350    
'''
# Corrigir com map
def convert_to_single_int(list_):
    string = ''

    for i in list_:
        string += str(i)

    return int(string)


'''    
43. Write a Python program to split a list into different variables.    
'''
def split_list(list_):
    a, b, c, *_ = list_

    return a, b, c, _


'''
44. Write a Python program to generate groups of five consecutive numbers in a list.
'''
def get_consecutive_numbers(list_):
    return  sorted(get_uniques(list_))[:5]


'''    
59. Write a Python program to check if the n-th element exists in a given list.
'''
# Corrigir
def check_element(list_, n):
    return False if len(list_) < n else True



if __name__ == '__main__':
    print(generate_sublist([1, 2, 3]))
