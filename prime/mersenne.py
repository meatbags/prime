# LucasLehmer mersenne primality test
# p must be an odd prime

import time
import math

def Mersenne(p):
    return (2 << (p - 1)) - 1

def LucasLehmer(p):
    M = Mersenne(p)
    s = 4
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    return s == 0

def ESieve(limit=-1, count=-1):
    primes = [2]
    n = 3
    while (n <= limit and limit != -1) or (len(primes) < count and count != -1):
        if not any(n % p == 0 for p in primes):
            primes.append(n)
        n += 2
    return primes

def CountDigits(n):
    return math.floor(math.log10(n) + 1)

#primes = ESieve(limit=50)
#print(primes)

primes = [2]
limit = 1000000
n = 3

while n < limit:
    # check prime
    if not any(n % p == 0 for p in primes):
        primes.append(n)
        now = time.time()

        # primality test
        if LucasLehmer(n):
            continue

        # print result
        M = Mersenne(n)
        digits = CountDigits(M)
        dt = math.floor((time.time() - now) * 10000) / 10000
        print('M' + str(n), M if digits < 32 else '*', '('+str(digits)+')', str(dt)+' s')

    # increment
    n += 2
