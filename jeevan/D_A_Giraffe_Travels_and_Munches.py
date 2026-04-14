def recur(i,j,step):
    if i >= n or j >= m:
        return -1000000
    if i == n-1 and j == m-1:
        return (3 * mat[i][j]) if step%2 == 0 else mat[i][j]
    
    if dp[i][j][step] != -1:
        return dp[i][j][step]
    
    opt_1 = recur(i+1,j+k,step+1)
    opt_2 = recur(i+k,j+1,step+1)
    dp[i][j][step] = max(opt_1,opt_2) + ((3 * mat[i][j]) if step%2 == 0 else mat[i][j])

    return dp[i][j][step]

n,m = map(int,input().split())
k = int(input())
dp = [[[-1 for i in range(200)] for i in range(m)] for i in range(n)]
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
mat[0][0] = 0
print(max(recur(0,0,0),-1))

