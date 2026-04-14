import sys
sys.setrecursionlimit(200005)
t = int(input())
for i in range(t):
    n = int(input())
    adj = [[] for i in range(n+1)]
    dist = [[] for i in range(n)]

    for i in range(n-1):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node,par,d):
        dist[d].append(par)
        for nbr in adj[node]:
            if nbr != par:
                dfs(nbr,node,d+1)

    dfs(1,0,0)
    ans = 0
    for lis in dist:
        ans = max(ans,len(lis) + (len(set(lis)) == 1))

    print(ans)
