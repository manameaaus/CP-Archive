t = int(input())
for i in range(t):
    n = int(input())
    d = []
    for i in range(n):
        d.append([input(),-(i+1)])
    d.sort()
    for i in d:
        print(-i[1],end=" ")
    print()