t = int(input())
for i in range(t):
    n = int(input())
    d = {}
    for i in range(n-1):
        x,y = map(int,input().split())
        d[x] = d.get(x,0) + 1
        d[y] = d.get(y,0) + 1

    x = list(d.values())
    if x.count(1) == min(n,2) and x.count(2) ==  max(n-2,0):
        print("Yes")
    else:
        if n == 1:
            print("Yes")
        else:
            print("No")