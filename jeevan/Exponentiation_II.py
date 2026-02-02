t = int(input())
MOD = 1000000000 + 7
for i in range(t):
    a,b,c = map(int,input().split())

    extra = 1
    while c > 0:
        if c & 1:
            extra = (extra * b) % (MOD-1)

        b = (b * b) % (MOD-1)
        c >>= 1


    ans = 1
    while extra > 0:
        if extra & 1:
            ans = (ans * a) % (MOD)
        a = (a * a) % (MOD)
        extra = extra >> 1

    print(ans)


