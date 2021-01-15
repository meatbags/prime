# P38

'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import math

def count_digits(n):
    return math.floor(math.log10(n) + 1)

def get_pandigital(n, digits):
    s = ''
    for d in digits:
        s += str(n * d)
    return int(s)

max_pan = 123456789

for lim in range(2, 10):
    digits = [ *range(1,lim+1) ]
    print('pan', digits)
    i = 1
    while True:
        pan = str(get_pandigital(i, digits))
        if len(str(pan)) == 9 and all(n in pan for n in '123456789'):
            print(pan)
            max_pan = max(int(pan), max_pan)
        if len(str(pan)) > 9:
            break
        i += 1

print('Max', max_pan)
