t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n-1):
        if not l[i] and not l[i+1]:
            print("YES")
            break
    else:
        if l.count(0) == 0:
            print("YES")
        else:
            print("NO")




