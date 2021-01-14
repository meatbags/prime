prime = [2]
lim = 10001
p = 3
while len(prime) != lim:
    if all([p % x != 0 for x in prime]):
        prime.append(p)
    p += 2
print(prime[-1])
