# Problem 97 -- Large non-mersenne prime

check = lambda n : str(28433 * (2 ** n) + 1)[-10:]
print(check(7830457))
