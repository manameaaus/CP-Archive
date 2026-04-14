n,k = map(int,input().split())

l = list(map(int,input().split()))
mat = []

for i in range(n):
    mat.append([l[i],i])

mat.sort(reverse = True)
for i in range(k):
    l[mat[i][1]],l[i] = l[i],l[mat[i][1]]
    

