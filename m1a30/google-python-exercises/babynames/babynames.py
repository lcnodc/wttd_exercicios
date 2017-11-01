#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    text = open(filename, 'r').read()
    year = re.search(r'\w+\s+\w{2}\s+(\d+)', text)

    print('Year: ' + str(year.group(1)))
    tuplas = re.findall(r'<td>(\w+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    print('RANK\t\tMALE NAME\t\tFEMALE NAME')

    for rank, male_name, female_name in tuplas[:50]:
        print('%s\t\t%s\t\t%s' % (rank, male_name, female_name))


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    if len(sys.argv) != 2:
        print('usage: ./babynames.py file-to-read')
        sys.exit(1)

    extract_names(sys.argv[1])


if __name__ == '__main__':
    main()
