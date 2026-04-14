import sys
sys.setrecursionlimit(4001)
t = int(input())
for i in range(t):
    n = int(input())
    l = [0,1] + list(map(int,input().split()))
    adj = [[] for i in range(n+1)]
    for u in range(2,n+1):
        v = l[u]
        adj[v].append(u)
    s = "L" + input()

    ans = [0]

    def dfs(node):
        black,white = 0,0
        for cld in adj[node]:
            b,w = dfs(cld)
            black += b
            white += w

        if s[node] == "B":
            black += 1
        else:
            white += 1

        ans[0] += white == black
        # print(node,black,white)
        return black,white
    
    dfs(1)
    print(ans[0])
    # print(adj)
        



