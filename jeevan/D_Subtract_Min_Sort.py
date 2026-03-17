t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(0,n-1):
        x = min(l[i],l[i+1])
        l[i] = l[i]-x
        l[i+1] = l[i+1]-x
    
    if l==sorted(l):
        ans = "YES"
    else:
        ans = "NO"
    print(ans)
