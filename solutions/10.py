lim = 2000000
prime = []
map = [1, 0] * int(lim / 2)
p = 3
while True:
    if not map[p]:
        is_prime = all([p % x != 0 for x in prime])
        if is_prime:
            for x in range(p, lim, p):
                map[x] = 1
            prime.append(p)
    p += 2
    if p > lim:
        break
acc = 2
for p in prime:
    acc += p
print(acc)
