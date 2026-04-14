t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    for i in range(n-1,-1,-2):
        c += i
    print(c+1)