t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    if m>n:
        print(m+1)
    else:
        print(n+1)