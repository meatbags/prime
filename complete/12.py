# 12

import math

number = 0
previous_number = 0
natural = 0

while True:
    # get next in sequence
    previous_number = number
    natural += 1
    number = previous_number + natural

    # count divisors
    divisors = 2
    lim = math.ceil(math.sqrt(number)) + 1
    for x in range(2, lim):
        if number % x == 0:
            divisors += 2

    # check done
    if divisors > 500:
        print('number:', number, 'divisors:', divisors)
        break
