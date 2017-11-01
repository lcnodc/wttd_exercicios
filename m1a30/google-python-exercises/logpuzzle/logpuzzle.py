#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    urls = []

    file_urls = open(filename, 'r')
    line = file_urls.readline()
    while line:
        match = re.search(r'GET\s(\D{1}\w{3}\D\w{9}\D+[^.ico][jpg]+)\sHTTP', line)
        urls
        if match and match.group(1) not in urls:
            urls.append(match.group(1))

        line = file_urls.readline()

    return sorted(urls)


def download_images(img_urls, dest_dir='test'):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on./home/luciano
    Creates an index.html in the directorydownload_images
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.isdir(dest_dir):
        os.system('mkdir ' + dest_dir )

    # for img in img_urls:
    #     urllib.request.urlretrieve(img_urls, dest_dir)

    with open(dest_dir +'/index.html', 'w') as f:
        f.write('<html>\n\t<body>')
        for img in img_urls:
            f.write("\n\t\t<img src='http://code.google.com" + img+ "'>")
        f.write('\n\t</body>\n</html>')


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    download_images(read_urls(args[0]))


if __name__ == '__main__':
    main()
