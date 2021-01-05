# 13

f = open('input/13.txt').readlines()
acc = 0
for line in f:
    acc += int(line)
res = str(acc)[:10]
print(res)
