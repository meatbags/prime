# Problem 69 -- Totient maximum

primes = [2]
n = 3
res = False
ratio = 1

def fuzzy(n, pf, ratio):
    res = n
    i = 0
    for p in pf:
        res *= 1 - (1 / p)
        i += 1
        if i == 3:
            break
    return n/res > ratio

def phi(n, pf):
    res = n
    for p in pf:
        res *= 1 - (1 / p)
    return int(res)

inc = 2

while n < 1000000:
    if not any(n % p == 0 for p in primes):
        primes.append(n)
    elif n % inc == 0:
        pf = [p for p in primes if n%p == 0]
        t = phi(n, pf)
        if n/t > ratio:
            ratio = n/t
            res = (n, t, ratio)
            inc = n
            print(res)
    n += 2

print(res)
