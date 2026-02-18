t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    l = l[::-1]
    ans = 0
    for i in range(0,n,2):
        ans += l[i]
    print(ans)