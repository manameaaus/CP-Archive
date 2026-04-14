t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    ans = 0
    dabba = []
    dp = [0] * (n+1)
    for i in range(m):
        l = list(map(int,input().split()))
        dabba.append(l)

    dabba = dabba[::-1]
    for i in range(m):
        l = dabba[i]
        x,y,v = l
        p_x = dp[x]
        p_y = dp[y]

        dp[x] = p_y + v
        dp[y] = p_x + v
        ans = max(ans,dp[x],dp[y])


    print(ans)


    

    

        
