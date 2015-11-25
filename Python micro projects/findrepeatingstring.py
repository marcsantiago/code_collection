def divisors(n):
    return (i for i in range(2, (n // 2) + 1) if n % i == 0)

def repeats(s):
    l = len(s)
    for d in divisors(l):
        spl = [s[i:i+d] for i in range(0, l, d)]
        if all(x == spl[0] for x in spl):
            return True
    return all(x == s[0] for x in s)