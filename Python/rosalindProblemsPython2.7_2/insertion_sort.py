def insertion_sort(arr):
    count = 0
    for i in xrange(1, len(arr)):
        j = i - 1
        key = arr[i]
        while (arr[j] > key) and (j >= 0):
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
    print(count)
    return arr