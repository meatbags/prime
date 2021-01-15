# P49

def isPermutation(a, b):
    str_a = str(a)
    str_b = str(b)
    return len(str_a) == len(str_b) and all(str_a.count(x) == str_b.count(x) for x in str(a))

def ESieve(lim=False, n=False):
    primes = [2]
    p = 3
    while (not lim or p < lim) and (not n or len(primes) < n):
        if not any(p % x == 0 for x in primes):
            primes.append(p)
        p += 2
    return primes

res = []
primes = [p for p in ESieve(lim=10000) if len(str(p)) == 4]
for i in range(len(primes) - 2):
    pi = primes[i]
    for j in range(i+1, len(primes)):
        pj = primes[j]
        if not isPermutation(pi, pj):
            continue
        pk = pj + (pj - pi)
        if pk in primes and isPermutation(pi, pk):
            res.append((pi, pj, pk))

for r in res:
    print(r, '->', ''.join([str(p) for p in r]))
