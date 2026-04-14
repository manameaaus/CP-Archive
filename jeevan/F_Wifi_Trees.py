t = int(input())
for i in range(t):
    n,m,x = map(int,input().split())
    ddd = min(m,n//2)
    print(ddd,x*ddd*(n-ddd))