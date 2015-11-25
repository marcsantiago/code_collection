num = int(input())
textArr = []
for i in range(0, num):
    text = input().upper()
    textArr.append(text)

for j in textArr:
    k = 0
    holes = 0
    while k < len(j):
        if j[k] in ['A', 'D', 'O', 'P', 'Q', 'R']:
            holes += 1
            k += 1
        elif j[k] == 'B':
            holes += 2
            k += 1
        else:
            k += 1
    print(holes)
