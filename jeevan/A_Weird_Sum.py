maxa = 100005
x = [[] for i in range(maxa)] 
y = [[] for i in range(maxa)] 
n,m = map(int,input().split())
for i in range(n):
    curr = list(map(int,input().split()))
    for j in range(m):
        x[curr[j]].append(i)
        y[curr[j]].append(j)

ans = 0

for i in range(maxa):
    length = len(x[i])
    x[i].sort()
    for j in range(length):
        ans += x[i][j] * (j + j - length + 1)

    length = len(y[i])
    y[i].sort()
    for j in range(length):
        ans += y[i][j] * (j + j - length + 1)



print(ans)
    
# print(x)


# 0  2
# -1 1

# 0 1
# -1 1