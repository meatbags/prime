# 26 Reciprocal Cycles

import math
import decimal

decimal.getcontext().prec = 5000

# find the smallest repeating element [0:n] in sequence
def getMinimumReciprocal(str):
    res = 0
    count = 0
    test = None
    length = len(str)
    lim = round(length / 2) + 1
    for i in range(1, lim):
        test = str[0:i]
        count = str.count(test)
        size = len(test)
        # 1. check repeating
        # 2. check approx. number of repeats is correct
        # 3. check pattern is immediately repeating
        if count > 1 and count >= math.floor(length / i):
            ok = True
            for j in range(0, length, size):
                if str[i] != str[j]:
                    ok = False
                    break
            if ok:
                res = size
                break
    return (res, test, count)

# find size of looping element in 1/d
def countCycles(d):
    number = str( decimal.Decimal(1) / decimal.Decimal(d) )
    res = [0, None]
    i = 0
    lim = len(number)
    while res[0] == 0 and i < lim:
        cycles = getMinimumReciprocal(number[i:lim])
        res = cycles
        i += 1
    return (d, number, 'n=', res[0], res[1], res[2])

res = [0, 0]
for d in range(1, 1000):
    cycles = countCycles(d)
    n = cycles[3]
    if n > res[1]:
        res[0] = d
        res[1] = n
        
        # print result
        print('D', d)
        print('Size', cycles[3])
        print('Pattern', cycles[4])
        print('Repeats', cycles[5])
        print()
