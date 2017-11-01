#!/usr/bin/env python

import os
import sys

# l = list(range(5))
#
# for i in l:
#     with open('file' + str(i) + '.html', 'w') as f:
#         f.write(
# """
# <html>
#     <body>
#         <img src="/edu/python/exercises/img0">
#         <img src="/edu/python/exercises/img1">
#         <img src="/edu/python/exercises/img2">
#     </body>
# </html>
# """)

def func1():
    l = list(range(5))
    urls = []

    for i in l:
        urls.append('http://code.google.com/edu/pages/image' + str(i) + '.jpg')

    with open('index.html', 'w') as f:
        f.write('<html>\n\t<body>')
        for url in urls:
            f.write("\n\t\t<img src='" + url + "'>")
        f.write('\n\t</body>\n</html>')


import operator

def func2():
    a = {'B2': 11.98, 'D2': 8.72, 'C1': 12.62, 'C2': 50.68}
    b = sorted(a.items(), key=operator.itemgetter(1), reverse=True)
    for c in b:
        print(c)


if __name__ == '__main__':
    func2()