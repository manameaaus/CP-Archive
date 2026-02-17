t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = len(set(a))
    y = len(set(b))
    if x*y<3:
        print("NO")
    else:
        print("YES")