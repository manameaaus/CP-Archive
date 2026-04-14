t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    a = l[0]
    e = l[-1]

    if a != -1 and e != -1:
        print(abs(e-a))
        print(*[i if i != -1 else 0 for i in l])
    else:
        print(0)
        if a == -1:
            l[0] = l[-1]
        else:
            l[-1] = l[0]
        print(*[i if i != -1 else 0 for i in l])


