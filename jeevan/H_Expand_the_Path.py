t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    res = len(s)+1

    R = s.count('R')+1
    D = s.count('D')+1

    if s[0] == 'D':
        if (R != 1):
            res += (n-D)*(n)
        res += (D-1)*(n-D)

        # print((n-D),(n))
        # print((D-1),(n-D))
        
    else:
        if (D != 1):
            res += (n-R)*(n)
        res += (R-1)*(n-R)

        # print((n-R),(n))
        # print((R-1),(n-R))

    print(res)