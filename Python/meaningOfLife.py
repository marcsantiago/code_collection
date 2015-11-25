#!/usr/bin/env python2.7

num = 0
arr = []
while num != 42:
    num = int(input())
    if num == 42:
        break
    else:
        arr.append(num)

for i in arr:
    print(i)
