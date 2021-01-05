# P30

import itertools
import math
import time

def eSieve(limit=-1, count=-1):
    primes = [2]
    n = 3
    while (n <= limit and limit != -1) or (len(primes) < count and count != -1):
        if not any(n % p == 0 for p in primes):
            primes.append(n)
        n += 2
    return primes

def countDigits(n):
    return math.floor(math.log10(n) + 1)

def sum5(digits):
    acc = itertools.accumulate([n ** 5 for n in digits])
    return [n for n in acc][-1]

def digitsIn(n):
    return len(str(n))

def getRange(digit):
    fifth = digit ** 5
    min = countDigits(fifth)
    max = countDigits(digit ** 5 * 5)
    return (min, max)
