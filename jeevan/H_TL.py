n,m = map(int,input().split())
l = list(map(int,input().split()))
x = list(map(int,input().split()))

j = max(max(l),min(l)*2)
if j < min(x):
    print(j)
else:
    print(-1)