# P32

'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234,
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

def is_pandigital_9(str):
    return all(i in str for i in '123456789')

def is_pandigital(a, b, c):
    n = str(a) + str(b) + str(c)
    return len(n) == 9 and is_pandigital_9(n)

found = []
sum = 0

for a in range(1, 99):
    for b in range(1, 9999):
        c = a * b
        if c not in found and is_pandigital(a,b,c):
            sum += c
            found.append(c)
            print(a,b,c)

print(sum)
