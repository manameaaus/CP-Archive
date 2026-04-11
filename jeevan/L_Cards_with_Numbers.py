n = int(input())
a = list(map(int,input().split()))
d = {}
for i in range(2*n):
    if a[i] in d:
        d[a[i]].append(i+1)
    else:
        d[a[i]] = [i+1]
c = sum(1 for i in d if len(d[i])%2)
if c:
    print(-1)
else:
    for i in d:
        for j in range(0,len(d[i]),2):
            print(d[i][j],d[i][j+1])


      