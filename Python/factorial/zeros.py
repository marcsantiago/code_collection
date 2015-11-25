import math

test = int(input())
arr = []
for i in range(0, test):
    num = int(input())
    arr.append(num)


for j in arr:
    powerFive = 1
    zeros = 0
    while powerFive < 1000000000:
        powerFive *= 5
        div = math.floor(j / powerFive)
        zeros += div
        if powerFive > j:
            break
    print(zeros)


