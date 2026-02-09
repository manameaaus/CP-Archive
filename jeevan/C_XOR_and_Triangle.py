t = int(input())
for i in range(t):
    n = int(input())
    x = bin(n)[2:]

    y = x.count("1")
    if y == 1 or y == len(x):
        print(-1)
    else:
        jo = x[::-1]
        one  =  jo.index("1")
        zero =  jo.index("0")
        ans = 2**one + 2**zero
        print(ans)

