# 2 2 5 5 6 6
# 3 1 4 3 1 4

# 2 1 5 3 6 4
# 3 2 4 5 1 6

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    new = set()
    newc = set()
    newd = set()
    c = []
    d = []
    x,y = a[-1],b[-1]
    
    for i in range(n):
        if i % 2:
            c.append(a[i])
            d.append(b[i])
        else:
            c.append(b[i])
            d.append(a[i])
    newc.add(c[-1])
    newd.add(d[-1])
    for i in range(n-2,-1,-1):
        if (c[i] in new or d[i] in new) or (c[i] in newc or d[i] in newd):
            print(i+1)
            break
        else:
            print(i,c[i],d[i])
            new.add(x)
            new.add(y)
            x,y = c[i],d[i]
            newc.add(c[i])
            newd.add(d[i])
    else:
        print(0)
    print(c)
    print(d)


