def track(idx,energy,time):
    if idx == n:
        return
    if go[idx][energy][time]:
        print(idx + 1,end = " ")
        track(idx+1,energy + mat[idx][1],time + mat[idx][2])
    else:
        track(idx+1,energy,time)
    
def recur(idx,energy,time):
    if energy > k or time > m:
        return -float('inf')
    if idx == n:
        return 0
    if dp[idx][energy][time] != -1:
        return dp[idx][energy][time]
    
    take = recur(idx+1,energy + mat[idx][1],time + mat[idx][2]) + mat[idx][0]
    not_take = recur(idx+1,energy,time)

    dp[idx][energy][time] = max(take,not_take)
    go[idx][energy][time] = take > not_take

    return dp[idx][energy][time]

n,k,m = map(int,input().split())
dp = [[[-1 for i in range(101)] for i in range(101)] for i in range(101)]
go = [[[-1 for i in range(101)] for i in range(101)] for i in range(101)]
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
print(recur(0,0,0))
track(0,0,0)


#     for j in range(101):
#         for k in range(101):
#             if j >= f and k >= t:
#                 dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-f][k-t] + v,dp[i][j-1][k-1] if j > 0 and k > 0 else 0,dp[i][max(j-1,0)][k] if j > 0 else 0)
#             else:
#                 dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k-1] if j > 0 and k > 0 else 0)
#             # if i == 5 and j == 60 and k == 10:
#             #     print(dp[i-1][j][k],dp[i-1][j-f][k-t])

# print(dp[n][k][m])
# print(dp[1][20][3])
# print(dp[2][20][3])
# print(dp[2][37][5])
# print(dp[2][38][5])