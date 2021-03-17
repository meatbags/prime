# P24 Lexicographic Permutations

import math

# get nth permutation
def get_permutation(list, n):
    n -= 1
    res = []
    list.sort()
    while len(list):
        limit = math.factorial(len(list))
        index = math.floor(n / limit * len(list))
        res.append(list[index])
        n -= math.floor(limit / len(list) * index)
        list = list[:index] + list[index+1:]
    return res

res = get_permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)
print(''.join(str(i) for i in res))

# permutation analysis
# import itertools
'''
def num_permutations(list):
    return math.factorial(len(list))

def num_permutations_repeats(list):
    d = 1
    checked = []
    for n in list:
        if n in checked:
            continue
        d *= math.factorial(list.count(n))
        checked.append(n)
    return math.factorial(len(list)) / d

def print_permutations(list):
    s = ''
    p = [ *itertools.permutations(list, len(list)) ]
    for n in p:
        s += ''.join(str(i) for i in n) + ' '
    print(s)

def analyse(list):
    p = [ *itertools.permutations(list, len(list)) ]
    first = int(''.join(str(i) for i in p[0]))
    prev = 0
    for tup in p:
        n = int(''.join(str(i) for i in tup))
        next = n - first
        print(next, next - prev, next / 9)
        prev = next
'''
