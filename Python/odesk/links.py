__author__ = 'marcsantago'
import urllib
import re

link = urllib.urlopen('https://wiki.python.org/moin/').read()
link_pattern = re.compile(r'''<a\s+(.*?)>(.*?)</a>''')

link_list = link_pattern.findall(link)

for l in link_list:
    print l