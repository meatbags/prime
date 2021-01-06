# Problem 20

n = str(math.factorial(100))
acc = 0
for i in range(len(n)):
    acc += int(n[i])
print(acc)
