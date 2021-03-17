import math
import random

# get random number
def rand():
    rand_max = 32767
    return random.randrange(rand_max + 1)

# count digits in n
def count_digits(n):
    return math.floor(math.log10(n) + 1)

# estimate iterations of n/2 until n=0
def estimate_div2_steps(n):
    a = 1
    count = 1
    while a < n:
        a <<= 1
        count += 1
    return count

# a * b % m
def mul_mod(a, b, m):
    x = 0
    y = a % m
    print('Estimated iterations', estimate_div2_steps(b))
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % m
        y = (y * 2) % m
        b = int(b / 2)
    return x % m

# modulo
def modulo(base, e, m):
    x = 1
    y = base
    print('Estimated iterations', estimate_div2_steps(e))
    while e > 0:
        if e % 2 == 1:
            x = (x * y) % m
        y = (y * y) % m
        e = int(e / 2)
    return x % m

# rabin-miller test
def miller(p, reps):
    if p < 2 or (p != 2 and p % 2 == 0):
        return False
    s = p - 1
    while s % 2 == 0:
        s = int(s / 2)
    for i in range(reps):
        a = rand() % (p - 1) + 1
        temp = s
        mod = modulo(a, temp, p)
        while temp != p-1 and mod != 1 and mod != p-1:
            mod = mul_mod(mod, mod, p)
            temp *= 2
        if mod != p-1 and temp % 2 == 0:
            return False
    return True


primes = []
for i in range(2, 100):
    if miller(i, 10):
        primes.append(i)

print(primes)
