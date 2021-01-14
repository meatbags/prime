# Problem 99 - Largest exponential

import math

f = open('input/99.txt')
lines = f.readlines()
baseExp = []
max = 0
res = 0

for i in range(len(lines)):
    line = lines[i]
    s = line.strip().split(',')
    if len(s) == 2:
        baseExp.append((int(s[0]), int(s[1])))
        base = int(s[0])
        exp = int(s[1]) / 100000
        n = math.pow(base, exp)
        if n > max:
            max = n
            res = (i+1, line)

print(res, max)
