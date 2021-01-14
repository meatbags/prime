# 8

import functools

input = open('input/8.txt').read()
res = 0
for i in range(0, len(input)-13):
    str = input[i:i+13]
    if str.find("0") == -1:
        list = [int(n) for n in str]
        res = max(res, functools.reduce(lambda a, b : a * b, list))
print(res)
