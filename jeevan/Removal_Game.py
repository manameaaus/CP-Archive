def recur(l,r,pos):
    if l == r:
        return arr[l] * pos

    if dp[l][r][pos] != -1:
        return dp[l][r][pos]
    
    x = recur(l+1,r,1-pos) + arr[l] * pos
    y = recur(l,r-1,1-pos) + arr[r] * pos

    if pos:
        dp[l][r][pos] = max(x,y)
    else:
        dp[l][r][pos] = min(x,y)

    return dp[l][r][pos]  

n = int(input())
arr = list(map(int,input().split()))
dp = [[[-1 for i in range(2)] for i in range(n)]for i in range(n)]
print(recur(0,n-1,1))


