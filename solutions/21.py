# 21

import math

def sumDiv(n):
    lim = n / 2
    x = 1
    sum = 0
    while x <= lim:
        if n % x == 0:
            sum += x
        x += 1
    return sum

map = {}
amicable = []
n = 1

while n < 10000:
    d = sumDiv(n)
    k = str(d)
    if k in map and map[k] == n:
        amicable.append((n, d))
    map[str(n)] = d
    n += 1

print(amicable)
print(sum(sum(pair) for pair in amicable))
