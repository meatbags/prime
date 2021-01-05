# 9

res = 0
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a ** 2 + b ** 2)
        sum = a + b + c
        if sum == 1000:
            print(a, b, c)
            res = a * b * c
            break
        elif sum > 1000:
            break
    if res:
        break
print(res)
