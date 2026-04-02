n,k = map(int,input().split())
mat = []
for i in range(n):
    a,b = map(int,input().split())
    mat.append([b,-a])

ans = 0
mat.sort()
for i in range(n):
    if mat[i][0]:
        if k:
            k -= 1
            ans -= mat[i][1]
        else:
            ans += mat[i][1]
    else:
        ans-=mat[i][1]

print(ans)



