__author__ = 'marcsantago'
import sys
import os
if len(sys.argv) != 2:
    print 'Usage: python commandline_test [filename]'
    sys.exit(1)

os.remove(sys.argv[1])