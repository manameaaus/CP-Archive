t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    if l.count(l[0]) == 4:
        print("YES")
    else:
        print("NO")