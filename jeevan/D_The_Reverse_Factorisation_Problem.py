import math
t = int(input())
for i in range(t):
    n = int(input())
    factors = list(map(int,input().split()))
    factors.sort()
    x = factors[0] * factors[-1]
    actual = []
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            actual.append(i)
            if actual[-1] != x//i:
                actual.append(x//i)

    actual.sort()

    if actual == factors:
        print(x)
    else:
        print(-1)