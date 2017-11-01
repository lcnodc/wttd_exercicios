#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
- Gerar 7000 números aleatórios
- Utilizando o intervalo entre 1000 e 3999
- Gerar valores aleatórios representando ambiente em uma lista de no máximo 10 tipos

"""

import random
import sys


def write_file(filename):
    ambientes = ['A', 'B', 'C', 'F', 'C2', 'D', 'E', 'I', 'B2']

    try:
        with open(filename, 'w') as file_to_write:
            for i in range(7000):
                print(random.randint(1001, 3999), random.choice(ambientes), file=file_to_write)
    except:
        file_to_write.close()
        sys.exit('Erros ao processar o arquivo')

    print("Arquivo gerado com sucesso!")


def make_dict(filename):

    fazendas = dict()

    with open(filename, 'r') as file_to_read:
        for linha in file_to_read:
            fazenda, ambiente = linha.split()
            ambientes = list()
            ambientes.append(ambiente)
            fazendas[fazenda] = fazendas.get(fazenda).append(ambiente) if fazendas.get(fazenda) else ambientes

    print(fazendas)



def main():
    if len(sys.argv) != 3:
        print("usage: ./ambientes.py {--write-to-file | --make-matrix} file")
        sys.exit(1)

    if sys.argv[1] == '--write-to-file':
        write_file(sys.argv[2])

    if sys.argv[1] == '--make-dict':
        make_dict(sys.argv[2])


if __name__ == "__main__":
    main()