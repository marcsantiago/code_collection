__author__ = 'marcsantago'
from bs4 import BeautifulSoup
import urllib
import sys


def find_links(seed):
    """Returns a list of links located on the seed page"""
    soup = BeautifulSoup(seed)
    link = list()
    for l in soup.find_all('a'):
        link.append(l.get('href'))
    return link


start = urllib.urlopen('http://www.marcsantiago.co.nf')
links = find_links(start)

for crawl in links:
    page = ''
    try:
        if crawl == 'http://www.marcsantiago.co.nf':
            page = urllib.urlopen(crawl)
    except:
        print(sys.stderr)
    soup = BeautifulSoup(page)
    for p in soup.find_all('p'):
        print p

