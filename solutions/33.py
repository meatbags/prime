# Problem 33

import math

ok = []
epsilon = 0

for n in range(10, 100):
    for d in range(10, 100):
        if d <= n:
            continue
        str_n = str(n)
        str_d = str(d)
        if str_n.count(str_n[0]) == 2 or str_d.count(str_d[0]) == 2:
            continue
        if str_n[0] != '0' and str_n.count(str_n[0]) == str_d.count(str_n[0]):
            a = int(str_n.replace(str_n[0], ''))
            b = int(str_d.replace(str_n[0], ''))
            if b != 0 and abs(n/d - a/b) <= epsilon:
                ok.append((n,d,a,b))
        if str_n[1] != '0' and str_n.count(str_n[1]) == str_d.count(str_n[1]):
            a = int(str_n.replace(str_n[1], ''))
            b = int(str_d.replace(str_n[1], ''))
            if b != 0 and abs(n/d - a/b) <= epsilon:
                ok.append((n,d,a,b))

print(' '.join(['{}/{}={}/{}'.format(x[0],x[1],x[2],x[3]) for x in ok]))
a = 1
b = 1
for x in ok:
    a *= x[0]
    b *= x[1]
gcd = math.gcd(a, b)
print('{}/{}'.format(a,b), 'GCD={}'.format(gcd), '{}/{}'.format(a/gcd, b/gcd))
