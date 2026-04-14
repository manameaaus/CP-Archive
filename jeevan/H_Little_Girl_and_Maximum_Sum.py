n , q = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
d = {}
for i in range(q):
    x,y = map(int,input().split())
    for i in range(x,y+1):
        if i in d:
            d[i]+=1
        else:
            d[i]=1

xx = list(d.values())
xx.sort(reverse=True)
ans = 0
for i in range(len(xx)):
    ans+=xx[i]*a[i]
print(ans)

