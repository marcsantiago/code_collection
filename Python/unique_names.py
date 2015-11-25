#! /urs/bin/env python2.7
__author__ = 'marcsantiago'
import os
import sys

start_folder = sys.argv[1]
#start_folder = "Target"

def check_folder_exist(folder):
    if os.path.exists(folder):
        return True
    else:
        return False

def get_files():
    """Grabs files from input folder"""
    file_path_list = []
    assert check_folder_exist(start_folder),\
    '''The Folder Entered Was Not Found, check spelling or path'''
    for files in os.listdir(start_folder):
        path = start_folder + "/" + files
        file_path_list.append(path)
    return file_path_list

old_files = get_files()

for f in old_files:
    taxa = []
    sequence = []
    with open(f, 'r') as data:
        lines = data.readlines()
    for l in lines:
        if l.startswith(">"):
            taxa.append(l)
        else:
            sequence.append(l)

    with open(f, 'w') as end_data:
        for i in xrange(len(taxa)):
            end_data.write(str(taxa[i]).rstrip() + str(i) + "\n")
            end_data.write(sequence[i])