# Stats

import itertools
import math
import random

def ProbFactorInSet(set):
    p = 0
    for i in range(len(set)):
        c = [ *itertools.combinations(set, i+1) ]
        sign = 1 if i % 2 == 0 else -1
        p += sign * sum(1 / math.prod(x) for x in c)
    return p

def ESieve(lim=False, n=False):
    primes = [2]
    p = 3
    while (not lim or p < lim) and (not n or len(primes) < n):
        if not any(p % x == 0 for x in primes):
            primes.append(p)
        p += 2
    return primes

def IsMersenne(p):
    return math.log2(p + 1) % 1 == 0

max = 20
print('Generating primes <', 1 << max)
primes = ESieve(lim=(1 << max))
print('Primes <', 1<<max, '=', len(primes))

for lim in range(3, max+1):
    tested = []
    found = []
    maxc = 1<<lim
    print('Primes <', maxc, '=', len([x for x in primes if x < maxc]))

    for n in range(2, lim+1):
        for m in range(2, n):
            c = (1 << n) - (1 << m) - 1
            if not c in tested:
                tested.append(c)
                if c in primes:
                    # print('2^'+str(n)+'-2^'+str(m)+'-1 =', str(1<<n)+'-'+str(1<<m)+'-1 =', c)
                    found.append(c)

    # print(found)
    a = len(found)
    b = len(tested)
    print('Max:', lim, 'Tested:', b, 'Primes:', a, 'P:', a/b if b != 0 else 0, end='\n\n')

# probability n divisible by first 20 primes = 0.8722 (~ 0.8722 simulation)
# probability n divisible by first 10000 primes ~ 0.95478 (simulation)
