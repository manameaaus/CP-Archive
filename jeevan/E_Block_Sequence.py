t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    for i in range(n-1,-1,-1):
        right = n - i - 1
        if arr[i] > right:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = min(dp[i + 1] + 1,dp[i + arr[i] + 1])

    print(dp[0])