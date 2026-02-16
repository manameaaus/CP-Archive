n = int(input())
l = list(map(int,input().split()))
if n == 1:
    print(1,1)
    print(0)
    print(1,1)
    print(0)
    print(1,1)
    print(-l[0])
else:
    print(1,n-1)
    for i in range(n-1):
        extra = l[i] % (n-1)
        full = l[i] // (n-1)
        x1 = n - (full % n)
        print((x1 + extra) * (n-1),end = " ")
        l[i] += (x1 + extra) * (n-1)
    print()
    print(2,n)
    for i in range(1,n-1):
        print(0,end = " ")
    extra = l[-1] % (n-1)
    full = l[-1] // (n-1)
    x1 = n - (full % n)
    l[-1] += (x1 + extra) * (n-1)
    print((x1 + extra) * (n-1),end = " ")
    print()
    print(1,n)
    for i in range(n):
        print(-l[i],end = " ")
    print()


