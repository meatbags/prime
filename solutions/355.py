# 355

import itertools

def eSieve(limit):
    primes = [2]
    n = 3
    while n <= limit:
        if not any(n % p == 0 for p in primes):
            primes.append(n)
        n += 2
    return primes

def coprime(a, b, primes):
    if a in primes or b in primes:
        return True
    primeFactors = [p for p in primes if a % p == 0]
    return not any(b % p == 0 for p in primeFactors)

def Co(n):
    primes = eSieve(n)
    coprimes = [p for p in primes]
    arr = []

    for i in range(len(coprimes)):
        p = coprimes[i]
        next = coprimes[i]

        # increment to maximum
        while next < n - p:
            next += p

        # reduce until arr is coprime
        while next != p and any(next % n == 0 and p != n for n in coprimes):
            next -= p

        # update list
        if next != p:
            coprimes[i] = next
            arr.append(coprimes[i])

    print([coprimes[i] for i in range(len(primes))])
    print(' '.join([str(primes[i]) + ':' + str(coprimes[i]) for i in range(len(primes))]))
    return sum(coprimes) + 1

print(10, Co(10))
print(30, Co(30))
print(100, Co(100))
