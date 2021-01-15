# Problem 23 - Non-abundant sums

import math

def get_divisors(n):
    lim = math.sqrt(n)
    divisors = [1]
    d = 2
    while d <= lim:
        if n % d == 0:
            divisors.append(d)
            if n / d != d:
                divisors.append(n / d)
        d += 1
    return divisors

def is_abundant(n):
    return sum(get_divisors(n)) > n

# get abundant numbers < 28123
abundant = []
limit = 28123
for i in range(1, limit+1):
    if is_abundant(i):
        abundant.append(i)
print('Abundant numbers:', len(abundant))
print(abundant[:30])

def is_abundant_sum(n):
    for i in range(len(abundant)):
        a = abundant[i]
        if a >= n:
            break
        b = n - a
        for j in range(len(abundant)):
            if abundant[j] == b:
                abundant_sums.append((n, a, b))
                return True
            elif abundant[i] > b:
                break
    return False

# get sums
abundant_sums = set()
for a in abundant:
    for b in abundant:
        abundant_sums.add(a+b)
print('Sums', abundant_sums)

res = []
for i in range(1, limit + 1):
    if not i in abundant_sums:
        res.append(i)

print(res[0:30], len(res))
print(sum(res))
