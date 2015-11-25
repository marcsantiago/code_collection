s = "D N A"
n = 3
count = 0
perm = ""
lst = s.split(" ")

def loop(lst, count):
    global perm
    if count < n:
        count += 1
        for s1 in lst:
            perm += s1
            print(perm)
            loop(lst, count)
            perm = perm[:-1]
    else:
        return

loop(lst, count)


