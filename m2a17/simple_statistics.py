#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Sua tarefa é processar uma seqüência de números inteiros para determinar as seguintes estatísticas:
    - Valor mínimo - OK
    - Valor máximo - OK
    - Número de elementos na seqüência: - OK
    - Valor médio - OK

Por exemplo para uma seqüência de números "6, 9, 15, -2, 92, 11", temos como saída:
    - Valor mínimo: -2
    - Valor máximo: 92
    - Número de elementos na seqüência: 6
    - Valor médio: 18.1666666
"""

import sys
from statistics import mean


def get_statistics(list_):
    list_ = list(map(int, list_))

    min_ = min(list_)
    max_ = max(list_)
    len_ = len(list_)
    avg_ = mean(list_)

    return ("""
        Min Value: {}
        Max Value: {}
        Length: {}
        Average: {}
    """.format(min_, max_, len_, avg_))


def main():
    if len(sys.argv) < 2:
        exit('usage: ./sum_multiples_below_of.py list')

    print(get_statistics(sys.argv[1:]))

if __name__ == '__main__':
    main()

