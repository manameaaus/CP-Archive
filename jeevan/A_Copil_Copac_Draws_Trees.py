import sys
sys.setrecursionlimit(200001)
t = int(input())
for i in range(t):
    n = int(input())
    adj = [[] for i in range(n+1)]
    rank = {}
    rank[(0,1)] = -1
    for i in range(n-1):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
        rank[(min(u,v),max(u,v))] = i



    
    def dfs(node,par,best):
        extra = (par == 0 or best > rank[(min(par,node),max(par,node))])
        # best = max(best,rank[(min(par,node),max(par,node))])
        best = rank[(min(par,node),max(par,node))]
        
        depth = 0
        for nbr in adj[node]:
            if nbr != par:
                depth = max(dfs(nbr,node,best),depth)

        
        # print(node,par,depth,extra)

        return depth + extra
    

    print(dfs(1,0,-1))
    
    # c = n-1
    # vis = [0] * (n+1)
    # while c:


    # 1 -> 2 -> 3 -> 4 -> 5
    
    # 3 4
    # 2 3
    # 1 2
    # 4 5


    # 1 -> 2

    # print(adj)


    # 1 2
    # 2 4

    # 2 5
    # 5 6
    # 2 3
    # 6 7




        
            
