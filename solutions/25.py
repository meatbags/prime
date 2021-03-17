
import math

def countDigits(n):
    return math.floor(math.log10(n) + 1)

last = 1
current = 1
index = 2
digits = 1

while digits < 1000:
    index += 1
    next = last + current
    last = current
    current = next
    digits = countDigits(current)

print(current)
print(digits, index)
