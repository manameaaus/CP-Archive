t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    
    ans = 0

    for i in range(0,n,2):
        if i == 0:
            ans += l[0] - min(l[0],l[1])
            l[0] = min(l[0],l[1])
        elif i == n-1:
            ans += l[i] - min(l[i-1],l[i])
            l[i] = min(l[i-1],l[i])
        else:
            ans += l[i] - min(l[i],l[i+1],l[i-1])
            l[i] = min(l[i],l[i+1],l[i-1])

    for i in range(1,n-1,2):
        if l[i] < (l[i-1] + l[i+1]):
            toremo = (l[i-1] + l[i+1]) - l[i]
            ans += toremo
            if l[i+1] >= toremo:
                l[i+1] -= toremo
            else:
                toremo -= l[i+1]
                l[i+1] = 0
                l[i-1] -= toremo

    # print(l)
    print(ans)

    
    
    
    