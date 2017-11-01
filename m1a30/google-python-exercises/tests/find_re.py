#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Search in the list of names, by a group that match with a regex, informed by user.

"""

import re
import sys

def find_regex(names):
    regex_ = input("Enter with a regex: ")
    message = 'Name {} {}match in the search by regex.'

    for name in names:
        if re.match(regex_, name):
            print(message.format(name, ''))
        else:
            print(message.format(name, 'not '))


def main():
    if len(sys.argv) < 2:
        sys.exit('usage ./find_re name ...')

    find_regex(sys.argv[1:])


if __name__ == "__main__":
    main()
