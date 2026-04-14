import sys
sys.setrecursionlimit(300001)

def recur(node,prev,count):
    ans[0] += prev + count
    vis[node] = 1
    temp_pre = 0
    temp_count = 0
    for nbr in adj[node]:
        if not vis[nbr]:
            fod = recur(nbr,temp_pre + prev + count,temp_count + count + 1)
            temp_pre += fod[0] + fod[1]
            temp_count += fod[1]
    
    return temp_pre,temp_count + 1


n = int(input())
adj = [[] for i in range(n+1)]
vis = [0 for i in range(n+1)]
l = list(map(int,input().split()))
for i in range(2,n+1):
    adj[i].append(l[i-2])
    adj[l[i-2]].append(i)
ans = [0]
for i in range(1,n+1):
    if len(adj[i]) == 1:
        # print(i)
        recur(i,0,0)
        break
print(ans[0])