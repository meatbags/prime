# 12

import math

prev = 0
i = 0
res = 0
max = 0

while True:
    next = prev + i
    lim = math.ceil(math.sqrt(next)) + 1
    n = 2
    for x in range(2, lim):
        if next % x == 0:
            n += 2
    prev = next
    i += 1
    if n > max:
        max = n
        print(next, ':', n)
    if n > 500:
        res = next
        break

print(res)
