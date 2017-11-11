#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Seqüência Look-and-Say


Este problema foi utilizado em 153 Dojo(s).
    A seqüência de números inteiros obtido a partir de um dígito (qualquer
        valor entre 1 e 9) onde o termo seguinte é obtido pela descrição do
        termo anterior é definida como uma seqüência look-and-say.

    Por exemplo, tendo como dígito inicial 1:
        - 1 é descrito como "um 1" ou 11;
        - 11 é descrito como "dois 1" ou 21;
        - 21 é descrito como "um 2, um 1" ou 1211;
        - 1211 é descrito como "um 1, um 2, dois 1" ou 111221;
        - 111221 é descrito como "três 1, dois 2, um 1" ou 312211.

    Para dígitos maiores ou iguais a 2, a seqüência é tem o seguinte formato:
        - d, 1d, 111d, 311d, 13211d, 111312211d (sendo d o dígito inicial).

    Dado o dígito inicial da seqüência, determine a soma de todos os dígitos
        do 50º elemento da seqüência.

3
13
1113
3113
123113
1112132113
21121113122113
122112311311222113
1122211213211321322113
213221121113122113121113222113
12111322211231131122211311123113322113
"""

# def conv_dict(list_):



def look_and_say(num):
    num_str = str(num)
    list_ = []
    quantity = 0
    value = 0
    ls = ''



    # if num == 1114:
    #     return '3114'
    #
    # if num == 1112:
    #     return '3112'
    #
    # if num == 1113:
    #     return '3113'

    for i in range(len(num_str)):
        if list_:
            if list_[i - 1].get(num_str[i]):
                list_[i - 1][i] = list_[i - 1].get(num_str[i]) + 1
            else:
                list_.append({num_str[i]: 1})
        else:
            list_.append({num_str[i] : 1})

    for i in list_:
        for c, v in i.items():
            ls += str(v) + str(c)
    return ls

if __name__ == '__main__':
    # assert look_and_say(3) == '13'
    # assert look_and_say(2) == '12'
    # assert look_and_say(4) == '14'
    # assert look_and_say(5) == '15'
    #
    # assert look_and_say(13) == '1113'
    # assert look_and_say(1113) == '3113'
    # assert look_and_say(1112) == '3112'
    # assert look_and_say(1114) == '3114'
    print(look_and_say(13))