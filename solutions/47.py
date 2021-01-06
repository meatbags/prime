# Problem 47 -- Distinct primes factors
res = False
primes = [2]
map = {}
n = 3

while True:
    factors = [p for p in primes if n % p == 0]
    if len(factors) == 0:
        primes.append(n)
    elif len(factors) == 4:
        map[str(n)] = 1
        if str(n-1) in map and str(n-2) in map and str(n-3) in map:
            res = n - 3
            break
    n += 1

print('Result:', res)
