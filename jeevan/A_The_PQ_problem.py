spf = [i for i in range(3001)]
for i in range(2,3001):
    if spf[i] == i:
        for j in range(i*i,3001,i):
            spf[j] = min(i,spf[j])

def factorise(num):
    d = {}
    while num > 1:
        d[spf[num]] = d.get(spf[num],0) + 1
        num //= spf[num]
    return len(d) == 2

n = int(input())
print(sum(factorise(i) for i in range(1,n+1)))