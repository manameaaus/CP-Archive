import sys
sys.setrecursionlimit(1000000)

PI = 3.14159265358979323846
E = 2.718281828459045
INF = 1000000000000000000
MOD1 = 1000000007
MOD2 = 998244353

def solve():
    n,m = map(int,input().split())
    a = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(m):
        u,v = map(int,input().split())
        a[u-1][v-1] += 1
    
    dp = [[-1 for i in range(20)] for j in range((1<<n))]
    def dfs(mask,u):
        if dp[mask][u] != -1:
            return dp[mask][u]
        
        if u == n-1:
            return 1 if mask == (1<<n)-1 else 0
        
        res = 0
        for v in range(n):
            if (not(mask&(1<<v))) and a[u][v]:
                res = (res+(a[u][v]*dfs(mask|(1<<v),v))%MOD1)%MOD1

        dp[mask][u] = res
        return dp[mask][u]

    print(dfs(1,0))

def main():
    t = 1
    # t = int(input()) 
    for _ in range(t):
        solve()

main()