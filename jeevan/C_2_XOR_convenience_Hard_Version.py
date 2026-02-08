def lsb(n):
    bit = 1
    while bit & n == 0:
        bit <<= 1
    return bit 
t = int(input())
for i in range(t):
    n = int(input())

    if n%2 == 1:
        res = [i for i in range(n+1)]
        for i in range(3,n+1,2):
            res[i],res[i-1] = res[i-1],res[i]

        res[1],res[-1] = res[-1],res[1]
        print(*res[1:])
    else:
        res = [i for i in range(n+1)]
        for i in range(3,n+1,2):
            res[i],res[i-1] = res[i-1],res[i]

        res[1],res[-1] = res[-1],res[1]
        lb = lsb(n)
        if n == lb:
            print(-1)
        else:
            res[lb],res[1] = res[1],res[lb]
            print(*res[1:])

