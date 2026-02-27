t = int(input())
for i in range(t):
    n = int(input())
    res = [i for i in range(n+1)]
    for i in range(3,n+1,2):
        res[i],res[i-1] = res[i-1],res[i]

    res[1],res[-1] = res[-1],res[1]
    print(*res[1:])