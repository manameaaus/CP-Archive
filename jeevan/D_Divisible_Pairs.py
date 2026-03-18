t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    l = list(map(int,input().split()))

    p = l[::]
    p.sort(key=lambda x:x%y)
    # p.append(p[-1]+1)

    ans = 0

    curr = p[0] % y
    d = {}
    for i in p:
        if i % y == curr:
            d[i%x] = d.get(i%x,0) + 1
        else:
            for key in d:
                if (x-key) % x == key:
                    ans += (d[key] * (d[key] - 1)) // 2
                else:
                    ans += d[key] * d.get(x-key,0)
                    if d.get(x-key,0) != 0:
                        d[x-key] = 0

            d = {}
            d[i%x] = 1
            curr = i%y

    for key in d:
        if (x-key) % x == key:
            ans += (d[key] * (d[key] - 1)) // 2
        else:
            ans += d[key] * d.get(x-key,0)
            if d.get(x-key,0) != 0:
                d[x-key] = 0

    print(ans)
    # print(*[(i%y) for i in p])
    # print(*p)
