t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    o = s.count("1")
    z = s.count("0")

    # if z == n:
    #     print(0)
    # elif z == 1:
    #     print(1)
    #     print(s.index("0")+1)
    # elif o == 2 and z > 0:
    #     k1 = s.index("1")
    #     k2 = s[::-1].index("1")
    #     print(2)
    #     print(k1+1,n-k2)
    # else:
    #     print(-1)

    zeros = []
    ones = []

    for i in range(n):
        if s[i] == "0":
            zeros.append(i+1)
        else:
            ones.append(i+1)
    if z%2 == 1 :
        print(z)
        print(*zeros)
    elif o % 2 == 0:
        print(o)
        if o:
        print(*ones) 
    else:
        print(-1)