# P39

import math

map = {};

def findSolutions(p):
    solutions = []
    for i in range(1,p):
        for j in range(1,p):
            k = math.hypot(i, j)
            if i + j + k != p:
                continue
            if not any(i in s and j in s and k in s for s in solutions):
                solutions.append((i,j,math.floor(k)))
    return solutions

max = -1
res = -1
for perimeter in range(1, 1001):
    solutions = findSolutions(perimeter);
    if len(solutions) > max:
        max = len(solutions)
        res = (perimeter, solutions, max)

print(res)
