t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    dp = [0] * n
    sufff = [0] * n

    curr = 0
    for i in range(n):
        if i == 0:
            if l[i] < 0:
                curr += l[i]
            else:
                curr += abs(l[i])
        else:
            curr += abs(l[i])

        dp[i] = curr

    curr = 0

    for i in range(n-1,-1,-1):
        curr -= l[i]
        sufff[i] = curr

    
    ans = -float('inf')
    for i in range(1,n-1):
        ans = max(ans,dp[i-1] + sufff[i+1])

    if n > 1:
        ans = max(ans,sufff[1])
        ans = max(ans,dp[n-2])
        

    print(ans)

