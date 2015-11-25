import itertools

list = []
user_input = int(input("Enter a number less then 7\n"))
if user_input == 1:
    list.append(1)
if user_input == 2:
    list.append(1)
    list.append(2)
if user_input == 3:
    list.append(1)
    list.append(2)
    list.append(3)
if user_input == 4:
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
if user_input == 5:
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
if user_input == 6:
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
if user_input == 7:
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)

e = len(list)
count = 0

for p in itertools.permutations(list, e):
    count += 1
    print(" ".join(map(str, p)))

print(count)



