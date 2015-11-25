from easygui import enterbox, msgbox, buttonbox
from sys import exit
import urllib2
import Tkinter



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
	r = Tkinter.Tk()
	r.withdraw()
	r.clipboard_clear()
	sentence = enterbox("Enter english sentence you would like to translate to Korean", title="Basic Korean Translator")
	translated_sentence = translate(sentence, 'ko')
	msgbox(translated_sentence)
	r.clipboard_append(translated_sentence)
	contin = buttonbox("Translate another message?", choices=["yes", "no"])
	if contin == "yes":
		r.destroy()
		continue
	elif contin == "no":
		r.destroy()
		exit(0)
