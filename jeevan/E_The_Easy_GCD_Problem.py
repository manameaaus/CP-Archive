import math
t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    suma = sum(l)
    res = 0
    curr = 0
    for i in range(n-1):
        curr += l[i]
        res = max(res,math.gcd(curr,suma-curr))
    print(res)

