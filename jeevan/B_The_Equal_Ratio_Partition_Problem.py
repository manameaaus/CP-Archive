import math
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    ans = 0
    freq = {}
    d = 0
    k = 0
    for i in s:
        if i == "D":
            d += 1
        else:
            k += 1

        g = math.gcd(d,k)
        td = d//g
        tk = k//g

        freq[(td,tk)] = freq.get((td,tk),0) + 1
        print(freq[(td,tk)],end = " ")

        # print(i,d,k,g)

    print()

    