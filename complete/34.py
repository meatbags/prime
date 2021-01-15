# Problem 34 -- Digit Factorials

import math

factorials = [math.factorial(i) for i in range(11)]
sum_factorials = lambda x : sum([factorials[int(s)] for s in str(x)])
res = []

for i in range(100000):
    if i == sum_factorials(i):
        res.append(i)
        print(i, sum_factorials(i))

print(res, sum(res) - 3)
