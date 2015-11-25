import re

def lang_identifier(variable_name):
    if not re.search(' ', variable_name) and not re.search('[A-Z]', variable_name) and not re.search('_', variable_name):
        return variable_name
    if variable_name.startswith('_'):
        return 'Error!'
    if re.search('_', variable_name):
        if re.search('[A-Z]', variable_name):
            return 'Error!'
        else:
            return 'c++'
    if re.search(' ', variable_name):
        return 'Error!'
    if not re.search('[A-Z]', variable_name):
        return 'Error!'
    else:
        return 'java'

while True:
    try:
        x = raw_input()
    except EOFError:
        break

    if lang_identifier(x) == 'Error!':
        print 'Error!'

    elif lang_identifier(x) != x:
        print x

    elif lang_identifier(x) == 'c++':
        cstringfirstword = ''
        clist = x.split('_')
        cstringfirstword += clist[0]
        del clist[0]
        cstring = ' '.join(clist).title()
        completecstring = cstringfirstword + cstring
        print completecstring.replace(' ', '')

    elif lang_identifier(x) == 'java':
        temp = [s for s in re.split("([A-Z][^A-Z]*)", x) if s]
        jstring = ' '.join(temp)
        print jstring.replace(' ', '_').lower()


