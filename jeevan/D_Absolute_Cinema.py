t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = [0] * n
    ff = l[0] - l[1]
    kk = 0
    for i in range(1,n-1):
        kk = l[i] - l[i+1]
        ans[i] = (ff - kk) // 2
        ff = kk
    
    ans[-1] = (l[0] - sum(i * ans[i] for i in range(n))) // (n-1)
    ans[0] = (l[1] - sum((i-1) * ans[i] for i in range(n)))
    print(*ans)
