#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    list_files = os.listdir(dir)
    try:
        for filename in list_files:
            if bool(re.search(r'__\w+__', filename)):
                print(os.path.abspath(os.path.join(dir, filename)))
    except:
        sys.stderr.write('Error while listing file.')


def copy_to(paths, dir):
    try:
        for path in paths:
            if os.path.isfile(path):
                shutil.copy(path, dir)
    except shutil.Error:
        sys.stderr.write('Error copying the file')

def zip_to(paths, zippath):
    files_to_zip = paths

    try:
        for path in paths:
            if os.path.isfile(path):
                files_to_zip.append(path)

        subprocess.Popen(['zip', '-j', 'arquivo.zip',] + files_to_zip,
                         stdout=subprocess.PIPE)
    except EOFError:
        sys.stderr.write('Errors occur during the process.')


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

        # +++your code here+++
        # Call your functions

if __name__ == "__main__":
    path = input('insert the source path: ')
    list_abspaths = []
    files = os.listdir(path)
    for file in files:
        list_abspaths.append(os.path.abspath(os.path.join(path, file)))

    dir = input('insert the destiny dir: ')
    copy_to(list_abspaths, dir)

    # dir = input("enter the dir: ")
    # get_special_paths('.')
    # main()