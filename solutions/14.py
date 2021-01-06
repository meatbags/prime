# 14

map = {}
map[1] = 1
res = {'i': 1, 'count': 0}

for i in range(1, 1000000):
    n = i
    count = 0
    while n not in map:
        count += 1
        n = n/2 if n%2 == 0 else 3*n + 1
    count += map[n]
    map[i] = count
    if count > res['count']:
        res['i'] = i
        res['count'] = count

print(res)
