# -*- coding: utf-8 -*-

'''
Escolhe 10 itens em um intervalo pré-definido.

Utiliza:
    - range
    - sample
    - sys

'''

import random
import sys

def samples(start, end, k_):
    list_ = list(range(int(start), int(end)))

    return sorted(random.sample(list_, int(k_)))[:]


def write_file(list_, dir_):
    list_ = ' '.join(list(map(str, list_)))

    try:
        with open(dir_ + '/' + 'choices.py', 'w') as file_:
            file_.write(list_)
    except FileNotFoundError:
        sys.exit('Diretório não encontrado.')


def main():
    if len(sys.argv) < 3:
        sys.exit('usage ./choices start end quantity dir')

    list_ = samples(sys.argv[1], sys.argv[2], sys.argv[3])
    dir_ = sys.argv[4]

    write_file(list_, dir_)

    sys.exit('Arquivo criado com sucesso!')


if __name__ == '__main__':
    args = ['python', '1', '24', '10', 'tuple' ]
    sys.argv = args
    main()