t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a)/n == x:
        print("YES")
    else:
        print("NO")