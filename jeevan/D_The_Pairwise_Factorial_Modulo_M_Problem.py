n,m = map(int,input().split())
l = list(map(int,input().split()))
s = set(l)
if len(s) != len(l) or len(l) > 1000:
    print(0)
else:
    ans = 1
    for i in range(n):
        for j in range(i+1,n):
            ans = (ans * abs(l[i]-l[j])) % m
    print(ans)

