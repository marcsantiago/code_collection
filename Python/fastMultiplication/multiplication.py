def main(n):
    curnum = 0
    while curnum < n:
        temp, temp2 = input().split()
        mul = int(temp) * int(temp2)
        yield mul
        curnum += 1

n = int(input())
for i in main(n):
    print(i)

