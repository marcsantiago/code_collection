__author__ = 'marcsantago'


def duplicate_checker(target, target_list):
    count = 0
    tar = str(target).replace('\n', '')
    tarlist = [str(i).replace('\n', '') for i in target_list]
    for i in tarlist:
        if tar == i:
            count += 1
    if count < 2:
        return True
    elif count >= 2:
        return False


def calculatepercent(string1, string2):
    string1 = str(string1).replace('\n', '')
    string2 = str(string2).replace('\n', '')
    count = 0
    for letter in xrange(len(string1)):
        if string1[letter] == string2[letter]:
            count += 1
    return round(float(count) / float(len(string1)), 3)


parsedfile = []
with open('errorcorrectionfile.txt') as data:
    for line in data.readlines():
        if line.startswith('>'):
            continue
        parsedfile.append(line)

copy = parsedfile
length_string = len(parsedfile[0])
list_length = len(parsedfile)

percentage = round((float((length_string - 1)) / float(length_string)), 1)

cop = []
p = []
for i in xrange(0, list_length):
    if duplicate_checker(copy[i], parsedfile):
        for j in xrange(0, list_length):
            if calculatepercent(copy[i], parsedfile[j]) == percentage:
                cop.append(copy[i])
                p.append(parsedfile[j])

newcop = [str(i).replace('\n', '') for i in cop]
newpar = [str(i).replace('\n', '') for i in p]

for j in xrange(0, len(newcop)):
    print(newcop[j], '->', newpar[j])
