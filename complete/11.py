# P11

f = open('input/11.txt').read()
input = [int(n) for n in f.split()]
vectors = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
];
res = 0
for x in range(3, 17):
    for y in range(3, 17):
        value = input[y * 20 + x]
        for v in vectors:
            vx, vy = v
            prod = value
            for i in range(1, 4):
                prod *= input[(y+vy*i) * 20 + (x+vx*i)]
            res = max(res, prod)
print(res)
