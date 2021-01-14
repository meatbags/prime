is_palin = lambda x : str(x) == str(x)[::-1]
min = 100 * 100
max = 999 * 999
res = 0
for n in range(max, min, -1):
    if is_palin(n):
        a = math.ceil(math.sqrt(n))
        b = a
        while a > 99 and b < 1000:
            while a * b < n:
                b += 1
            while a * b > n:
                a -= 1
            if a * b == n:
                break
        if a * b == n:
            print(a, b, n)
            res = n
            break
print(res)
