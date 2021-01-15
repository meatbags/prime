# Problem 22

import itertools

f = open("input/22.txt").read().strip().split(',')
off = ord('A') - 1
names = sorted([name.replace('"', '') for name in f])
name_sum = lambda name : sum([ord(letter) - off for letter in name])
res = sum([name_sum(names[i]) * (i + 1) for i in range(len(names))])
print(res)
