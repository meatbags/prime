# 35 -- Circular Primes

import itertools

primes = open('input/primes_sub_1M.txt').read().split(',')
circular = []

for p in primes:
    if any(int(c) % 2 == 0 for c in p) and p != '2':
        continue
    circ = True
    rot = p
    for i in range(len(p)-1):
        rot = rot[1:] + rot[0]
        if not rot in primes:
            circ = False
            break
    if circ:
        circular.append(p)

print(circular)
print(len(circular))
