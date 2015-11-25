#!/usr/bin/env python2.7
__author__ = 'marcsantiago'


def outfile_exist():
    import os
    if os.path.exists('outfiles'):
        return True
    else:
        return False


def get_file_names():
    import os
    assert outfile_exist(),\
        '''The directory 'outfiles' does not exist or is not in the same directory as python script'''
    for i in os.listdir('outfiles'):
        if i.endswith('.out'):
            yield i


def parse_dot_out_file():
    """Iterates over files locates in the directory 'outfiles' and pulls out names that are both unique and are below
    the E value 1e-20"""
    import re

    for out_file in get_file_names():
        out = 'outfiles/'+out_file
        record = open(out, 'r')
        E_VALUE_THRESH = (1 * 10) ** -20
        comp_pattern = re.compile('comp')

        parse_from_file = 'junkdata/parsed_from_outfile_'+out_file.replace('.out', '')+'.txt'
        with open(parse_from_file, 'w') as parse:
            for line in record.readlines():
                if line.startswith('>'):
                    continue
                if re.search(comp_pattern, line):
                    parse.write(line)

        formatting = list()
        with open(parse_from_file, 'r') as reformat:
            for dup in reformat.readlines():
                formatting.append(dup.split())

        # Takes the name and the E value and stores them respectively
        exp = list()
        name = list()
        for i in xrange(len(formatting)):
            name.append(formatting[i][0])
            exp.append(str(formatting[i][len(formatting[i]) - 1:]).replace('[', '').replace(']', '').replace("'", ''))
        name2 = list()
        for counter in xrange(len(name)):
            name2.append(''.join(name[counter]))
        name = name2

        exp = [float(i) for i in exp]

        #sorts through the list and removes all cases where the e value is above E_VALUE_THRESH
        trimmed_names = []
        trimmed_exp = []
        for j in xrange(len(formatting)):
            if exp[j] <= E_VALUE_THRESH:
                trimmed_names.append(name[j])
                trimmed_exp.append(exp[j])

        #removes duplicates and creates a value list for each unique key
        id_exp = dict()
        for k, v in zip(trimmed_names, trimmed_exp):
            id_exp[k] = id_exp.get(k, []) + [v]

        output_file = 'uniquenames/'+out_file.replace('.out', '')+'_done'+'.txt'
        with open(output_file, 'w') as final_data:
            for keys in id_exp.keys():
                final_data.write(keys)
                final_data.write('\n')
