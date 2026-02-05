t = int(input())
for i in range(t):
    n,h,k = map(int,input().split())
    l = list(map(int,input().split()))
    pre = l[::]
    suf = l[::]

    left = l[:]

    for i in range(1,n):
        pre[i] = min(pre[i-1],pre[i])
        left[i] += left[i-1]
    for i in range(n-2,-1,-1):
        suf[i] = max(suf[i+1],suf[i])


    tot = left[-1]

    ans = (h // tot) * (n+k)
    h %= tot

    if h:
        for i in range(n):
            ans += 1
            if (left[i] >= h) or (left[i] - pre[i] + suf[i+1] >= h):
                break
    else:
        ans -= k
    
    print(ans)
        
