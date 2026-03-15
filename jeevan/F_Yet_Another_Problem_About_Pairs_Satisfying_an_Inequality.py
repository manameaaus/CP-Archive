t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))

    dp = [0] * n
    for i in range(n):
        if l[i] <= i:
            dp[i] += 1
        if i:
            dp[i] += dp[i-1]

    ans = 0
    for i in range(n):
        if l[i] <= i:
            if (l[i]-2 >= 0):
                ans += dp[l[i]-2]

    print(ans)


    