t = int(input())
for i in range(t):
    n,m,a,b = map(int,input().split())
    rem = (n*m) - max(((b-1) * n),((a-1) * m),((m-b) * n),((n-a) * m))
    rem = 45
    # print(rem)
    c = 0
    while rem != 1:
        if rem % 2 == 0:
            rem = rem // 2
        else:
            rem = rem // 2 + 1
        c += 1
    print(c)

