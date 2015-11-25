#!/usr/bin/env python2.7
__author__ = 'marcsantiago'


def target_exist():
    import os
    if os.path.exists('Targets'):
        return True
    else:
        return False


def get_uniquenames():
    import os
    for i in os.listdir('uniquenames'):
        if i.endswith('.txt'):
            yield i


def get_targets():
    import os
    assert target_exist(),\
        '''The directory 'Targets' does not exist or is not in the same directory as python script'''
    for i in os.listdir('Targets'):
        if i.endswith('.fasta'):
            yield i


def parse_targets():
    import re

    target_file_list = list()
    for targets in get_targets():
        target_file_list.append(targets)

    sequence_file_list = list()
    for sequences in get_uniquenames():
        sequence_file_list.append(sequences)

    for index in xrange(len(target_file_list)):
        target_file_path = 'Targets/' + target_file_list[index]
        with open(target_file_path, 'r') as target_file:
            target_list = target_file.read().split('>')
        sequence_file_path = 'uniquenames/' + sequence_file_list[index]
        with open(sequence_file_path, 'r') as sequence_file:
            sequence_list = sequence_file.read().split()

        output_file_name = 'fastafiles/' + str(target_file_list[index]).replace('Trinity', 'Done')
        with open(output_file_name, 'w') as output:
            for tar in target_list:
                for seq in sequence_list:
                    match = re.match(seq, tar)
                    if match:
                        output.write(tar)
