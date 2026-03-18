MAXN = 100001

spf = [i for i in range(MAXN)]
for i in range(2,MAXN):
    if spf[i] == i:
        for j in range(i*i,MAXN,i):
            spf[j] = min(i,spf[j])

def factorise(num):
    d = {}
    while num > 1:
        d[spf[num]] = d.get(spf[num],0) + 1
        num //= spf[num]
    return sorted(d.items())

n,k = map(int,input().split())
l = list(map(int,input().split()))
reuse = [[] for i in range(n)]
ans = 0
d = {}
useless = [0] * n

perfect = 0

for i in range(n):
    num = l[i]
    factors = factorise(num)
    reuse[i] = factors
    temp = []

    for prime,power in factors:
        if power%k:
            temp.append((prime,power%k))
    if temp:
        temp = tuple(temp)
        d[temp] = d.get(temp,0) + 1
    else:
        perfect += 1
        useless[i] = 1
    

for i in range(n):
    num = l[i]
    factors = reuse[i]
    temp = []

    if useless[i]:
        continue

    valid = 1

    for prime,power in factors:
        if (power%k):
            temp.append((prime,k-(power%k)))
            if power%k != k-(power%k):
                valid = 0

    temp = tuple(temp)
    ans += d.get(temp,0) - valid


print(ans//2 + (perfect * (perfect - 1) // 2))



