# Problem 40 -- Champernowne's constant

s = ''
d = [1, 10, 100, 1000, 10000, 100000, 1000000]
n = 1
res = 1

while len(s) < d[-1]:
    s += str(n)
    n += 1

for i in range(len(d)):
    index = d[i] - 1
    res *= int(s[index])

print(res)
