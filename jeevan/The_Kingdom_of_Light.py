import math
def log(n):
    x = int(math.log(n,3))
    ans = 0
    while n>0:
        y = n // (3**x)
        if y == 2:
            ans += 1
        n %= (3**x)
        x -= 1
    return ans

n = (10**6)+1
l = [0]*(n+1)
ans = 0
for i in range(2,n):
    ans += log(i)
    l[i] = ans
# print(l[:8])
# print(log(1000000))

t = int(input())
for i in range(t):
    n = int(input())

    print(l[n])

