t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    d = {}
    d[0] = 3
    d[1] = 1
    d[2] = 2
    d[3] = 1
    d[5] = 1
    for i in range(n):
        if a[i] in d:
            d[a[i]] = max(d[a[i]]-1,0)
        if sum(d.values()) == 0:
            print(i+1)
            break
    else:
        print(0)

