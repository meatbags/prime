# Search

import math
import decimal

f = open('utils/primes1000.txt')
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
    return (2 << exp) - (2 << n) - 1

def test(exp, n, prime):
    candidate = generateNumber(exp, n)
    if candidate % prime == 0:
        print('2^' + str(exp), '- 2^' + str(n), '- 1')
        print('Failed %', prime)
        return False
    return True

# probability that a random digit <= 100000000 digits is prime .00000004342
# using odd numbers .00000008684

# 100,000,001 digits
exp = 332192811
test = [_ for _ in range(1, 1000)]


# Prime #575: 4201 Passed: 26
# Candidates less than 100 tested up to Prime #575 (4201)
# [1, 3, 9, 13, 15, 19, 22, 25, 30, 34, 39, 40, 45, 51, 54, 58, 63, 66, 73, 75, 78, 88, 90, 91, 93, 94]

# Testing against prime #239: 1499
# Prime #239: 1499 Passed: 241
test = [3, 9, 13, 15, 19, 22, 25, 30, 34, 39, 40, 45, 51, 54, 58, 63, 66, 69, 73, 75, 78, 81, 88, 90, 91, 93, 94, 106, 109, 112, 115, 121, 123, 126, 130, 141, 142, 145, 150, 153, 159, 160, 162, 171, 178, 181, 183, 186, 189, 193, 195, 201, 210, 211, 214, 219, 225, 229, 231, 232, 235, 238, 243, 249, 253, 255, 259, 265, 270, 273, 286, 289, 303, 306, 315, 318, 321, 322, 331, 333, 339, 342, 345, 346, 349, 354, 355, 373, 375, 378, 379, 381, 382, 385, 390, 393, 394, 400, 402, 403, 405, 409, 411, 418, 423, 426, 429, 435, 438, 441, 450, 451, 459, 471, 474, 475, 483, 493, 498, 502, 505, 510, 519, 522, 523, 526, 531, 534, 538, 544, 546, 549, 553, 555, 558, 561, 562, 565, 571, 579, 582, 585, 591, 592, 598, 601, 606, 615, 618, 619, 625, 630, 639, 643, 651, 654, 661, 664, 666, 670, 673, 675, 678, 682, 690, 691, 693, 699, 705, 706, 715, 718, 723, 729, 733, 735, 739, 745, 750, 753, 754, 760, 762, 763, 769, 774, 781, 783, 786, 789, 790, 793, 805, 808, 810, 813, 819, 822, 825, 831, 834, 835, 841, 843, 846, 849, 850, 855, 865, 870, 873, 879, 880, 883, 885, 886, 889, 891, 894, 898, 903, 913, 918, 922, 925, 931, 933, 939, 942, 945, 949, 951, 952, 958, 961, 963, 970, 973, 985, 990, 999]
start = 239

for i in range(start, 1000):
    p = primes[i]
    print("Testing against prime #" + str(i+1) + ":", p)
    test = [n for n in test if test(exp, n, prime)]
    print("Prime #" + str(i+1) + ":", prime, "Passed:", len(test))
    print([n[2] for n in test], end="\n\n")

# 1 Billion Digits
# exp = 3321928095
# Passed #119
# passed = [3, 7, 13, 15, 16, 18, 21, 27, 30, 40, 43, 45, 46]
# for i in range(119, 1000):
#    prime = [primes[i]]
#    print('Testing against prime #' + str(i) + ':', prime[0])
#    passed = [m for m in passed if testAgainst(exp, m, prime)]
#    print(passed)
