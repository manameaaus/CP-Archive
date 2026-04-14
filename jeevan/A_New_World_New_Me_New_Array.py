import math
t = int(input())
for i in range(t):
    n,k,p = map(int,input().split())
    k = abs(k)
    p = abs(p)
    if p*n>=k:
        print(math.ceil(k/p))
    else:
        print(-1)