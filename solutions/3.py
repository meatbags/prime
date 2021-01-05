# Problem 3

import math
import time

primes = [2, 3]

def isPrime(number):
    if any(number % p == 0 for p in primes):
        return False
    lim = math.sqrt(number)
    n = primes[-1]
    while n <= lim:
        if not any(n % p == 0 for p in primes):
            primes.append(n)
        if number % n == 0:
            return False
        n += 2
    return True

now = time.time()
factors = []
result = False
composite = 600851475143
lim = math.sqrt(composite)
n = 3

while n <= lim:
    if composite % n == 0:
        if isPrime(n):
            factors.append(n)
    n += 2

print(factors)
result = max(factors)
dt = time.time() - now
print('Result:', result, dt)
