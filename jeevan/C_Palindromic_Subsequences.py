t = int(input())
for i in range(t):
    n = int(input())
    l = [0]*n
    l[0] = 1
    l[2] = 1
    l[n-1] = 1
    c = 2
    for i in range(n):
        if i==0 or i==2 or i==n-1:
            continue
        else:
            l[i] = c
            c+=1
    print(*l)