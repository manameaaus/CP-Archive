dp = [[0,0] for i in range(51)]
dp[0][1] = 1
def f(n):
    if n == 1:
        dp[1] = [5,3]
        return dp[1]
    t,p = f(n-1)
    dp[n] = [2*t+3,2*p+1]
    return dp[n]

f(50)


n,x = map(int,input().split())
res = 0
l = n
while x:
    if x == dp[l][0]:
        res += dp[l][1]
        break
    elif x < dp[l][0]:
        pass
    else:
        x -= 1
        

print(res)



