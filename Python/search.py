#!/usr/bin/env python

'''
Finding files by pattern
'''

import os
import fnmatch
from os.path import join


def search(base, patt):
    ''' Yield files that match a given pattern '''
    for root, dirs, files in os.walk(base):
        try:
            for _ in [join(root, _) for _ in files if fnmatch.fnmatch(_, patt)]:
                yield _
        except IOError as error:
            print error


def example_use(d, p):
    ''' Example use of search function '''
    for _ in search(d, p):
        print _


if __name__ == '__main__':
    example_use('/Users/marcsantago', '*.log')