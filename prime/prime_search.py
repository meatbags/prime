# Search

import math
import decimal
import time

f = open('input/primes1000.txt')
primes = [int(n) for n in f.read().split(',')]
primes10 = primes[:10]
primes100 = primes[10:100]
primes1000 = primes[100:1000]

def countDigits(n):
    return math.floor(math.log10(n) + 1)

def approxPrimes(exp):
    base = 2
    n = base << exp
    return n / n * math.log(base)

def findExponent(n):
    exp = 1
    inc = 1000000
    digits = countDigits(2 << exp)

    while True:
        while digits < n:
            exp += inc
            digits = countDigits(2 << exp)
        inc //= 10
        while digits > n:
            exp -= inc
            digits = countDigits(2 << exp)
        inc //= 10
        if digits == n:
            return exp

def generateNumber(exp, n):
    return (1 << exp) - (1 << n) - 1

def test(exp, n, prime):
    candidate = generateNumber(exp, n)
    if candidate % prime == 0:
        print('2^' + str(exp), '- 2^' + str(n), '- 1')
        print('Failed %', prime)
        return False
    return True

# 100,000,001 digits
exp = 332192812
candidates = [ *range(0, 1000) ]
start = 1

print("Start")
time_start = time.time()
for exp in range(100000):
    n = (1 << exp) - 1
    r = n % 7
print(time.time() - time_start)

# Testing against prime #966: 7603
# Prime #966: 7603 Passed: 191
# [4, 10, 14, 16, 20, 23, 31, 35, 40, 41, 46, 52, 59, 64, 67, 74, 79, 89, 91, 92, 94, 95, 107, 110, 113, 116, 122, 124, 127, 131, 142, 151, 154, 160, 163, 172, 179, 182, 184, 190, 194, 196, 202, 211, 212, 215, 220, 226, 230, 232, 233, 236, 239, 244, 250, 254, 256, 260, 271, 274, 287, 290, 304, 307, 316, 323, 340, 343, 347, 355, 356, 374, 376, 379, 380, 382, 386, 395, 401, 403, 404, 406, 410, 427, 430, 436, 439, 442, 452, 460, 472, 475, 476, 484, 494, 499, 506, 511, 523, 524, 527, 532, 535, 547, 554, 559, 562, 566, 572, 580, 586, 592, 593, 599, 602, 607, 616, 619, 626, 631, 640, 644, 652, 655, 662, 665, 667, 674, 676, 679, 683, 691, 692, 694, 700, 707, 716, 724, 730, 734, 736, 740, 746, 751, 754, 755, 761, 763, 764, 770, 775, 782, 784, 787, 790, 809, 820, 826, 832, 835, 836, 851, 856, 866, 871, 880, 881, 884, 886, 887, 890, 899, 904, 914, 919, 926, 932, 934, 940, 943, 946, 952, 953, 959, 962, 964, 971, 974, 986, 991, 1000]
# start = 965


#for i in range(start, 1000):
#    prime = primes[i]
#    print("Testing against prime #" + str(i+1) + ":", prime)
#    candidates = [n for n in candidates if test(exp, n, prime)]
#    print("Prime #" + str(i+1) + ":", prime, "Passed:", len(candidates))
#    print(candidates, end="\n\n")
