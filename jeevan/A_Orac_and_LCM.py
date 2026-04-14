import math
MAXN = 200005

spf = [i for i in range(MAXN)]
for i in range(2,MAXN):
    if spf[i] == i:
        for j in range(i*i,MAXN,i):
            spf[j] = min(i,spf[j])

primes = {}

def factorise(num):
    # print(num)

    d = {}
    while num > 1:
        d[spf[num]] = d.get(spf[num],0) + 1
        num //= spf[num]
    # print(d)
    for prime in d:
        power = d[prime]
        if prime in primes:
            primes[prime].append(power)
        else:
            primes[prime] = [power]
    
    


n = int(input())
l = list(map(int,input().split()))
ans = 1
for i in l:
    factorise(i)
for prime in primes:
    if len(primes[prime]) == n:
        primes[prime].sort()
        ans *= math.pow(prime,primes[prime][1])
    elif len(primes[prime]) == n-1:
        primes[prime].sort()
        ans *= math.pow(prime,primes[prime][0])


print(int(ans))
# print(primes)
