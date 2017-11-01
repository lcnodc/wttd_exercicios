#!/usr/bin/env python

import random
import sys

def write_file(filename):
    with open(filename, 'w') as file_to_write:
        for n in range(100):
            print(str(random.randint(1, 100)), end=' ', file=file_to_write)


def make_matrix(filename):
    matrix = list()
    linhas = list()
    colunas = list()

    file_to_read = open(filename, 'r')
    text_file = file_to_read.readlines()
    for line in text_file:
        it = iter(line.split())
        for n in it:
            matrix.append([n, next(it)])

    for l in matrix:
        print(' ', l)


def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
    for j in range(n_colunas):
        linha += [valor]

        # coloque linha na matriz
        matriz += [linha]

    return matriz


def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("usage: ./matrix.py {--write-to-file | --make-matrix} file")
        sys.exit(1)

    if args[0] == '--write-to-file':
        write_file(args[1])

    if args[0] == '--make-matrix':
        make_matrix(args[1])


if __name__ == "__main__":
    # print(crie_matriz(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    main()