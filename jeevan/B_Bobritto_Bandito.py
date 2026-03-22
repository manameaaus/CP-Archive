t = int(input())
for i in range(t):
    n,m,l,r = map(int,input().split())
    if abs(l) >= m:
        print(-m,0)
    else:
        print(l,l+m)
    