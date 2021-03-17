lim = 2000000

def jim_seive(lim):
    primes = [True]*lim
    sump = 0
    highp = 0
    p = 2
    while p**2 < lim:
        for i in range(p**2,lim,p):
            primes[i] = False
        p = p + 1
    for i in range(2,lim):
        if primes[i] == True:
            sump += i
            highp = i
    print('Highest prime',highp,'Sum',sump)

def xavier(lim):
    map = [0] * lim
    acc = 2
    for p in range(3, lim+1, 2):
        if not map[p]:
            for x in range(p, lim, p*2):
                map[x] = 1
            acc += p
    print(acc)

jim_seive(lim)
xavier(lim)
