t = int(input())
for i in range(t):
    n = int(input())
    new = [i+1 for i in range(1,n+1)]
    new[-1] = 1
    print(*new)