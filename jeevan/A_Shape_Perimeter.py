t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    peri = 4*m
    xl = []
    yl = []
    for i in range(n):
        x,y = map(int,input().split())
        xl.append(x)
        yl.append(y)
    xsum = sum(xl[1:])
    ysum = sum(yl[1:])
    peri += 2*(xsum+ysum)
    print(peri)
