__author__ = 'marcsantago'
import insertion_sort
f = open('merge.txt', 'r').readlines()
l1 = f[1].split()
l2 = f[3].split()

merged = l1 + l2
print insertion_sort.insertion_sort(merged)