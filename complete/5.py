# 5

prime = [1, 2, 3, 5, 7, 11, 13, 17, 19]
nonprime = [x for x in range(1, 21) if x not in prime]
lcm = functools.reduce(lambda a, b : a * b, prime)
n = lcm
while True:
    if all(n % x == 0 for x in nonprime):
        break
    n += lcm
print(n)
