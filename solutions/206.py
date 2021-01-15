# P206

import math

input = "1_2_3_4_5_6_7_8_9_0"

def match(n):
    str_n = str(n)
    return len(str_n) == len(input) and all(input[i] == '_' or str_n[i] == input[i] for i in range(len(input)))

min_x = 1010101010
max_x = 1389026623
for x in range(min_x, max_x, 10):
    x2 = x * x
    if (match(x2)):
        print(x, x2)
        break


'''
input = "1_2_3_4"
digits = math.floor(len(input) / 2)
limit = 10 ** digits

def getNum(n):
    str_n = str(n)
    res = input[::-1]
    while len(str_n):
        res = res.replace("_", str_n[0], 1)
        str_n = str_n[1:]
    res = res[::-1]
    return int(res.replace("_", "0"))

for i in range(limit):
    num = getNum(i)
    if math.sqrt(num) % 1 == 0:
        print(math.sqrt(num), num)
        break
'''
