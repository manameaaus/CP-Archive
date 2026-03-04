# 2 2 2 2 3 3 3
# 2 2 4 4 5 5 5

t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    d = {}
    for i in b:
        d[i] = d.get(i,0) + 1

    st = 1

    l = [[] for i in range(n+1)]

    for i in d:
        if d[i] % i :
            print(-1)
            break
        for k in range(d[i]//i):
            for j in range(i):
                l[i].append(st)
            st += 1
    else:
        for i in b:
            print(l[i].pop(),end= " ")
        print()

    

    




    