#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Formata meu relatório contendo setor, fazenda, talhao, ambiente e area.

Esse script tem como objetivo transpor um relatório de colunas para
linhas, gerando um novo arquivo.

- antes: uma fazenda para um ambiente
- depois: uma fazenda para vários ambientes

Além disso, com ele é possível estudar um pouco o funcionamento dos
dicionários, em python 3.

"""

import sys
import operator


def return_percent(fazendas):
    for fazenda, ambientes in fazendas.items():
        area_total = sum(ambientes.values())
        for ambiente in ambientes:
            percent = float(ambientes.get(ambiente)) / area_total
            fazendas.get(fazenda)[ambiente] = round(percent * 100, 2)

    return fazendas


def main(filename):
    fazendas = dict()

    with open(filename, 'r') as arquivo_leitura:
        for line in arquivo_leitura:
            setor = int(line.split()[0])
            fazenda = int(line.split()[1])
            talhao = int(line.split()[2])
            solo = line.split()[3]
            area = float(line.split()[4])

            ambientes = {solo: float(area)}
            if fazendas.get(fazenda):
                if fazendas.get(fazenda).get(solo):
                    fazendas.get(fazenda)[solo] = \
                        float(fazendas.get(fazenda).get(solo)) + float(area)
                else:
                    fazendas.get(fazenda)[solo] = area
            else:
                fazendas[fazenda] = ambientes

    with open('fazendas.txt', 'w') as arquivo_escrita:
        fazendas = return_percent(fazendas)
        for fazenda, ambientes in fazendas.items():
            ambientes_ordenados = sorted(ambientes.items(), key=operator.itemgetter(1), reverse=True)
            texto = ''
            for i in ambientes_ordenados:
                texto += str(i[0]) + '=' + str(i[1]) + ' '
            print(fazenda, texto , file=arquivo_escrita)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: ./agrupa_ambiente --file-to-read")
        sys.exit(1)

    main(sys.argv[1])