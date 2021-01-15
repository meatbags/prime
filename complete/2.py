fib = [1, 2]
lim = 4000000
while True:
    x = fib[-1] + fib[-2]
    if x >= lim:
        break
    fib.append(x)
res = sum([x for x in fib if x%2 == 0])
print(res)
