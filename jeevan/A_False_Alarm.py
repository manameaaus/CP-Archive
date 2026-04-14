t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    yy = l[::-1]
    if n-yy.index(1) - l.index(1) > x:
        print("NO")
    else:

        print("YES")