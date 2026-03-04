n = int(input())
a = list(map(int,input().split()))
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
ans = 0
for i in d:
    ans += d[i]*(d[i]-1)/2


for i in range(n):
    x = a[i]
    ans -= d[x]*(d[x]-1)/2
    d[x]-=1
    ans += d[x]*(d[x]-1)/2
    print(int(ans))
    ans -= d[x]*(d[x]-1)/2
    d[x]+=1
    ans += d[x]*(d[x]-1)/2



    
