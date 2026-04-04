t = int(input())
for i in range(t):
    n = int(input())
    up = list(map(int,input().split()))
    down = list(map(int,input().split()))


    mele = []
    kelage = []

    mina = up[0]
    maxa = up[0]

    for i in range(n):
        mina = min(mina,up[i])
        maxa = max(maxa,up[i])
        mele.append([mina,maxa])

    mina = down[n-1]
    maxa = down[n-1]

    for i in range(n-1,-1,-1):
        mina = min(mina,down[i])
        maxa = max(maxa,down[i])
        kelage.append([mina,maxa])

    kelage = kelage[::-1]

    dp = [float("inf")] * (2 * n + 1)
    dp2 = [-1 ] * (2 * n + 1)


    ans = 0
    for i in range(n):
        mina = min(mele[i][0],kelage[i][0])
        maxa = max(mele[i][1],kelage[i][1])
        # ans += mina * (2*n - maxa + 1)

        dp[mina] = min(dp[mina],maxa)
        dp2[maxa] = max(dp2[maxa],mina)

        # print(mina,maxa)


    

    for i in range(1,2*n + 1):
        if dp[i] != float("inf"):
            ans += i * (2 * n - dp[i] + 1)

    ans2 = 0

    for i in range(1,2*n + 1):
        if dp2[i] != -1:
            ans2 += dp2[i] * (2 * n - i + 1)

    ans3 = 0


    if dp[2*n] != float("inf"):

        ans3 = 2 * n - dp[2 * n] + 1


    for i in range(2 * n - 1 ,0,-1):
        dp[i] = min(dp[i],dp[i+1])
        if dp[i] != float("inf"):
            ans3 += 2 * n - dp[i] + 1




    # print(dp)
    # print(dp2)

    
    # print(ans,ans2)
    print(ans3)
    # print(ans2)