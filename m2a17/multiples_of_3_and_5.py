#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3
    or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

from functools import partial
import sys


multiple_of = lambda divisor, dividend: dividend % divisor == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def sum_multiples_below_of(num):
    sum_ = 0

    for i in range(1, num):
        if multiple_of_3(i) or multiple_of_5(i):
            sum_ += i

    return sum_


def main():
    if len(sys.argv) != 2:
        exit('usage: ./sum_multiples_below_of.py number')

    number = int(sys.argv[1])
    print(sum_multiples_below_of(number))


if __name__ == "__main__":
    main()
