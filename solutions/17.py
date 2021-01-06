# Problem 17

w19 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
n19 = [len(x) for x in w19]
wTens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
nTens = [len(x) for x in wTens]
n100 = len("hundred")
n1000 = len("thousand")
nAnd = len("and")
total = 0

for i in range(1, n+1):
    word = ""
    sum = 0
    if i == 1000:
        word = "one thousand"
        sum += n19[1] + n1000
    elif i >= 100:
        index = math.floor(i / 100)
        sum += n100 + n19[index]
        word += w19[index] + " hundred "
        if i % 100 != 0:
            word += "and "
            sum += nAnd
    last2 = i % 100
    if last2 != 0:
        if last2 <= 19:
            word += w19[last2]
            sum += n19[last2]
        else:
            index = math.floor(last2 / 10)
            word += wTens[index] + " " + w19[last2 % 10]
            sum += nTens[index] + n19[last2 % 10]
    total += sum
    # print(word, sum)

print("Result", total)
