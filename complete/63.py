# Problem 63 -- Powerful digit counts

import math

def countDigits(n):
    return math.floor(math.log10(n) + 1)

d = 1
acc = 0

while True:
    n = 1
    count = 0
    res = []
    while True:
        pow = n ** d
        digits = countDigits(pow)
        if digits > d:
            break
        if digits == d:
            count += 1
        n += 1
    print('digit', d, 'count', count, res)
    if count == 0:
        break
    acc += count
    d += 1

print('total', acc)
