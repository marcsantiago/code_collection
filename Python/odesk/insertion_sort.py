__author__ = 'marcsantago'


def insertion_sort(seq):
    count = 0
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1
            count += 1
    print seq
    return count


lis = open('data.txt', 'r').read().split()
lis = [int(i) for i in lis]
print insertion_sort(lis)