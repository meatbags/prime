# Problem 29 -- Distinct powers
# a^b for 2 ≤ a ≤ n and 2 ≤ b ≤ m:

def distinct(n, m):
    terms = set()
    for a in range(2, n+1):
        for b in range(2, m+1):
            terms.add(a**b)
    return len(terms)

print(distinct(5, 5))
print(distinct(100, 100))
