t = int(input())
for i in range(t):
    n,h = map(int,input().split())
    a = list(map(int,input().split()))
    l = [[0,0] for i in range(n)]
    r = [[0,0] for i in range(n)]

    l[0] = [h,-1]
    r[-1] = [h,n]

    maxa = a[0]
    idx = 0
    for i in range(1,n):
        if a[i] >= maxa:
            maxa = a[i]
            idx = i
        l[i] = [maxa,idx]


    maxa = a[-1]
    idx = n-1

    for i in range(n-2,-1,-1):
        if a[i] >= maxa:
            maxa = a[i]
            idx = i
        r[i] = [maxa,idx]



    dp = [0] * n

    # print(l)
    print(r)


    for i in range(n):
        eta = (n * h) - ((a[i]) * n) - ((l[i][0] - a[i]) * (l[i][1]+1)) - ((r[i][0] - a[i]) * (n - r[i][1]))
        # for j in range(l[i][1]+1,r[i][1]):
        #     eta -= max(0,a[j]-a[i])
        hhh = 0
        for j in range(i-1,l[i][1],-1):
            hhh = max(hhh,a[j])
            eta -= max(0,hhh-a[i])

        hhh = 0
        for j in range(i+1,r[i][1]):
            hhh = max(hhh,a[j])
            eta -= max(0,hhh-a[i])
        dp[i] = eta

    ans = 0
    print(dp)

    for i in range(n):
        exp = dp[i]
        kkk = 0
        for j in range(l[i][1]):
            exp = max(exp,dp[i]+dp[j]- dp[l[i][1]])
            # kkk = max(kkk,dp[j])
        for j in range(r[i][1]+1,n):
            # kkk = max(kkk,dp[j])
            exp = max(exp,dp[i]+dp[j]-dp[r[i][1]])


        ans = max(ans,exp)

        # print(ans,i)


    print(ans)


    