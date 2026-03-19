t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    d = {}
    ans = 0
    for i in range(n):
        d[arr[i]]=i+1
    for i in d.values():
        ans+=i
    print(ans)
    print(d)