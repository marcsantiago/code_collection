#!/usr/bin/env python2.7
# -*- coding: latin-1 -*-
import urllib2
import sys


def translate(to_translate, to_langage="auto", langage="auto"):
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result



while True:
	to_translate = raw_input("Enter English Sentence or type q to exit\n")
	if to_translate != 'q':
		print("%s >> %s" % (to_translate, translate(to_translate, 'ko')))
	else:
		sys.exit(0)
