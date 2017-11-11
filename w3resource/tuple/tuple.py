#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercises: 4 5 6 9 12 13 15 16 19 23
'''

'''
4. Write a Python program to unpack a tuple in several variables. 
'''
def unpack_tuples(t):
    a, b, c, *_ = t

    return a, b, c, _


'''
5. Write a Python program to add an item in a tuple. 
'''
def add_tuple_item(t, i):
    t += (i,)
    return t


'''
6. Write a Python program to convert a tuple to a string.
'''
def convert_to_string(t):
    return ' '.join(map(str, t))


'''    
7. Write a Python program to get the 4th element and 4th element from last of a tuple.


8. Write a Python program to create the colon of a tuple.



9. Write a Python program to find the repeated items of a tuple.
'''
def find_the_repeated(t):
    repeated = tuple()

    for i in t:
        if t.count(t[i]) > 1:
            if t[i] not in repeated:
                repeated += (t[i],)

    return repeated


'''
10. Write a Python program to check whether an element exists within a tuple.



11. Write a Python program to convert a list to a tuple.



12. Write a Python program to remove an item from a tuple.
'''
def remove_item(t, i):
    t_ =  t[:1] + t[1 + 1:]

    # ou converter uma tupla para lista.
    t_ = list(t).remove(i)


'''
13. Write a Python program to slice a tuple.
'''
def slice_tuple(t):
    return t[0:5], t[5:7], t[7:]


'''
14. Write a Python program to find the index of an item of a tuple.



15. Write a Python program to find the length of a tuple.
'''
def find_the_length(t):
    return len(t)


'''
16. Write a Python program to convert a tuple to a dictionary.
'''
def convert_to_dict(t):
    dict_ = dict()
    i = iter(t)

    for x in i:
        # dict_[i] = v
        # Desta forma, estamos iterando duplamente na tupla, agora já um iterable
        # e utilizando o primeiro elemento como chave e o segundo como valor.
        dict_.update({x: next(i)})

    return dict_


'''
17. Write a Python program to unzip a list of tuples into individual lists.



18. Write a Python program to reverse a tuple.


19. Write a Python program to convert a list of tuples into a dictionary.

'''
#
def convert_to_dict2(list_):
    dict_ = {}

    # desempacotar a tupla simplifica o acesso a seus itens.
    for x, y in list_:
        #dict_[x] = dict_.get(x) + [y,] if dict_.get(x) else [y,]
        # Set default é mais eficiente, pois sempre retorna o valor.
        # Desta forma, podemos add o novo item à lista retornada.
        dict_.setdefault(x, []).append(y)

    return dict_

if __name__ == '__main__':
    print(convert_to_dict2([("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]))

'''
20. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)



21. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]



22. Write a Python program to replace last value of tuples in a list.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']



23. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
'''
from operator import itemgetter

def sort_list_tuple(list_):
    return sorted(list_, key=itemgetter(1), reverse=True)


# if __name__ == '__main__':
#     print(sort_list_tuple([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]))

'''
24. Write a Python program to count the elements in a list until an element is a tuple.

'''
