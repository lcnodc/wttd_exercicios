
# -*- coding: utf-8 -*-

'''
Exercises dict.

'''

'''
1. Write a Python script to sort (ascending and descending) a dictionary by value.
'''
from operator import itemgetter

def dict_sort(dict_):
    return sorted(dict_.items(), key=itemgetter(1))


'''
4. Write a Python script to check if a given key already exists in a dictionary. 
'''
def check_key(dict_, key_):
    # Por padrão, o dicionário retorna as chaves, assim, não é necessário
    # utilizar o método keys()
    return key_ in dict_.keys()


'''
10. Write a Python program to sum all the items in a dictionary. 
'''
# Items são os valores.
def sum_dict_items(dict_):
    return sum(dict_.values())


'''
14. Write a Python program to sort a dictionary by key. 
'''
def dict_sort(dict_):
    # return sorted(dict_.items(), key=itemgetter(0))
    # Outra solução seria ordenar as chaves e puxar os valores a partir
    # da nova lista.
    for i in sorted(dict_):
        print(i, dict_.get(i))



'''
15. Write a Python program to get the maximum and minimum value in a dictionary.
'''
def get_min_max(dict_):
    return min(dict_.values()), max(dict_.values())


'''
18. Write a Python program to check a dictionary is empty or not.
'''
def is_empty(dict_):
    # return 'is empty: {}'.format(len(dict_) == 0)
    return bool(dict_)


'''
26. Write a Python program to count the values associated with key in a dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
'''
def ckeck_success(list_):
    # Não precisava testar já que False é igual a 0.
    # return sum([1 for i in list_ if i.get('success')])
    return sum(i['success'] for i in list_)


'''
28. Write a Python program to sort a list alphabetically in a dictionary. 
'''
def list_alphabet():
    num = {'n1': [2 , 3 , 1] , 'n2': [5 , 1 , 2] , 'n3': [3 , 2 , 4]}
    [num.get(k).sort() for k in num]
    return num


'''
32. Write a Python program to print a dictionary line by line.
'''
def print_dict():
    students = {'Aex': {'class': 'V' ,
                        'rolld_id': 2} ,
                'Puja': {'class': 'V' ,
                         'roll_id': 3}}
    for c1, v1 in students.items():
        print('{}'.format(c1))
        for c2, v2 in v1.items():
            print(c2, v2)


'''
35. Write a Python program to sort Counter by value.
Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
'''
def dict_sort2(dict_):
    t = (())

    for k, v in dict_.items():
        t += (k, v),

    return t


'''
38. Write a Python program to convert a dictionary to OrderedDict.

'''
from collections import OrderedDict

def convert_to_ordered(dict_):
    return OrderedDict(dict_)


if __name__ == "__main__":
    print_dict()
