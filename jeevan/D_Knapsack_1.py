n,m = map(int,input().split())
value = []
weight = []
for i in range(n):
    w,v = map(int,input().split())
    value.append(v)
    weight.append(w)

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n+1):    
    for j in range(m+1):
        if i==0 and j==0:
            dp[i][j] = 0
        elif weight[i-1]<=j:
            dp[i][j] = max(value[i-1]+dp[i-1][j-weight[i-1]],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp)

    