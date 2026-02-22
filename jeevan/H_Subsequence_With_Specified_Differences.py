n,k = map(int,input().split())
arr = list(map(int,input().split()))
allowed = list(map(int,input().split()))

dp = {}
ans = -1
for i in range(n):
    for j in range(k):
        dp[arr[i]] = max(dp.get(arr[i],1),dp.get(arr[i]-allowed[j],0) + 1)
    ans = max(ans,dp[arr[i]])


print(ans)