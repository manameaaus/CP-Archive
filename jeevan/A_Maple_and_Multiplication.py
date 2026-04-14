import math
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    k = (math.lcm(a,b))
    if a == k and b == k:
        print(0)
    elif a==k or b ==k:
        print(1)
    else:
        print(2)
