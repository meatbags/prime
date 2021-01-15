# p98 -- anagramatic squares

import math

def countDigits(n):
    return math.floor(math.log10(n) + 1)

def getAnagrams(word, list):
    length = len(word)
    anagrams = []
    for w in list:
        if w == word or length != len(w):
            continue
        if all(word.count(l) == w.count(l) for l in word):
            anagrams.append(w)
    return anagrams

def getLargestSquare(word, anagram, squares):
    shortlist = []
    passed = []
    length = len(word)
    filtered = []

    # get shortlist of matching squares
    for sqr in squares:
        if all(word.count(word[i]) == sqr.count(sqr[i]) for i in range(length)):
            shortlist.append(sqr)

    # check anagram is square number
    for sqr in shortlist:
        if sqr in filtered:
            continue
        a = list(anagram)
        for i in range(length):
            a[a.index(word[i])] = sqr[i]
        a = "".join(a)
        if a in squares:
            passed.append(int(a))
            filtered.append(a)

    # return max | 0
    if len(passed) == 0:
        return 0
    res = max(passed)
    print(word, anagram, res)
    return res

words = [w.replace('"', '') for w in open("input/98.txt").read().split(",")]
filtered = []
dict = {}
max_length = 0

# get first anagram
for w in words:
    if w in filtered:
        continue
    a = getAnagrams(w, words)
    if len(a) > 0:
        dict[w] = a[0]
        max_length = max(len(w), max_length)
        filtered.append(a[0])

# build square map digits:[squares]
max_number = int("9" * max_length)
n = 1
squares = {}
while True:
    sqr = n ** 2
    if sqr > max_number:
        break
    digits = str(countDigits(sqr))
    if not digits in squares:
        squares[digits] = []
    squares[digits].append(str(sqr))
    n += 1

max_square = 0

for word in dict:
    digits = str(len(word))
    max_square = max(getLargestSquare(word, dict[word], squares[digits]), max_square)

print(max_square)
