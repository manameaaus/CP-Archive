n,m = map(int,input().split())
include = []
not_include = []

for i in range(m):
    l = list(map(int,input().split()))
    if l[1]:
        include.append(l+[i])
    else:
        not_include.append(l+[i])

include.sort()
not_include.sort()


ans = [[] for i in range(m)]
maxa = [0]*(n+1)
for i in range(2,n+1):
    maxa[i] = include[i-2][0]
    ans[include[i-2][2]] = [i-1,i]



tar = len(not_include)
alloted = 0
for i in range(3,n+1):
    for j in range(i-2,0,-1):
        if alloted == tar:
            break
        if not_include[alloted][0] >= maxa[i]:
            ans[not_include[alloted][2]] = [j,i]
            alloted += 1
        else:
            break
    if alloted == tar:
            break

if alloted == tar:
    for i in ans:
        print(*i)
else:
    print(-1)

        