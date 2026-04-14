t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    req = 1
    ans = 0

    for i in l:
        if i == req:
            req += 1
        else:
            ans += 1

    print((ans + k - 1) // k)