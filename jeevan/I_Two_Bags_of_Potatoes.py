y, k, n = map(int,input().split())
h = k - y%k
if h + y > n:
    print(-1)
else:
    while h <= n - y:
        print(h,end=" ")
        h += k
