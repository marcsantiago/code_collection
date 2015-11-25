import math

test = int(input())
arr = []
for i in range(0, test):
    num = int(input())
    arr.append(num)

for j in arr:
    print(math.factorial(j))



