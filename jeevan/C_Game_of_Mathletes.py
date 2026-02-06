t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    le = 0
    r = n-1
    c = 0
    while r>le:
        if l[r]+l[le]==k:
            c+=1
            le+=1
            r-=1
        elif l[r]+l[le]>k:
            r-=1
        elif l[r]+l[le]<k:
            le +=1
    print(c)

