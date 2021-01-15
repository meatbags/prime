# Problem 44 -- Pentagon Numbers

import math

def pent(n):
    return (n * (3 * n - 1)) / 2

def get_pents(min, max):
    pents = []
    for i in range(min, max + 1):
        pents.append(pent(i))
    return pents

def find_pair_in(a, list):
    for b in list:
        if a+b in pents and abs(b-a) in pents:
            return (a, b, abs(b-a))
    return False

def find_pair(n):
    i = pents.index(n)
    return find_pair_in(n, pents[i+1:])

pents = get_pents(1, 10000)
print(pents[:30])
d = -1

for a in pents:
    res = find_pair(a)
    if res:
        print(res)
        break;

print('Result:', d)
