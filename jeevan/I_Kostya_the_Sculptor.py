t = int(input())
d = {}
maxa = []
su = 0

for i in range(t):
    x = sorted(map(int,input().split()))
    y = str(x[1])+","+str(x[2])
    cu = 0
    got = []
    if y in d:
        if len(d[y]) == 1:
            if x[0] > d[y][0][0]:
                d[y].append([x[0],i+1])
            else:
                d[y].insert(0,[x[0],i+1])
        else :
            if x[0] > d[y][0][0] and x[0] > d[y][1][0]:
                d[y][0] = d[y][1]
                d[y][1] = [x[0],i+1]
            else:
                d[y][0] = [x[0],i+1]
        cu = d[y][0][0] + d[y][1][0]
        got = [d[y][1][1] , d[y][0][1]]
    else:
       d[y] = [[x[0],i+1]]
       cu = x[0]
       got = [i+1]
    
    if min(cu,x[1],x[2]) >= su:
        su = min(cu,x[1],x[2])
        maxa = got

print(len(maxa))
print(*maxa)