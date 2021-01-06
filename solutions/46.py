# Problem 46 -- Goldbach's other conjecture

import math

check = lambda n, p: math.sqrt((n - p) / 2) % 1 == 0
res = False
primes = [2]
n = 3

while True:
    if all(not n % p == 0 for p in primes):
        primes.append(n)
    elif not any(check(n, p) for p in primes):
        res = n
        break
    n += 2

print(res)
