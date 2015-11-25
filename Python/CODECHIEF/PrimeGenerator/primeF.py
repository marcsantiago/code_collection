import math


class Main(object):
    def __init__(self):
        self.N_MAX = 1000000000
        self.n_sqrt = int(math.sqrt(self.N_MAX))
        self.primes = []
        self.generatePrime(self.n_sqrt)

    def generatePrime(self, n):
        arr = [True] * (n + 1)
        for i in xrange(2, n + 1):
            if arr[i]:
                self.primes.append(i)
                for j in range(i * i, n + 1, i):
                    arr[j] = False

    def output(self, m, n):
        arr = [True] * (n - m + 1)
        x = n - m + 1
        stop = int(math.sqrt(n))
        for p in self.primes:
            if p > stop:
                break
            m_dash = max(int(math.ceil(m / float(p)))*p, p*p)
            for j in xrange(m_dash, n + 1, p):
                arr[j - m] = False
        for i in xrange(x):
            if arr[i] and m+i != 1:
                print(m + i)

    def solve(self):
        tests = int(raw_input())
        for test in xrange(tests):
            m, n = map(int, raw_input().split())
            self.output(m, n)
            print

Main().solve()