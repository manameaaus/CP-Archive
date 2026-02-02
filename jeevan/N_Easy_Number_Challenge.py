def divisors(n):
    l = [1]*(n+1)
    for i in range(2, n+1):
        for j in range(i,n+1,i):
            l[j] += 1
    return l
a,b,c = map(int,input().split())
d = divisors(a*b*c)
ans = 0
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            ans += d[i*j*k]
print(ans)