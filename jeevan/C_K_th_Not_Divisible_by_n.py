t  = int(input())
for i in range(t):
    n,k = map(int,input().split())
    curr = k - k%n
    c = (curr // n) * (n-1)
    req = k - c
    curr += req//(n-1) * n
    req  = req%(n-1)
    curr += req
    if curr % n == 0:
        print(curr-1)
    else:
        print(curr)

