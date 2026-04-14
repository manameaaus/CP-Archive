t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))

    ref = [0] * n
    for i in range(n-1):
        if l[i] < 2 * l[i+1]:
            ref[i] += 1

    mina = n
    ans = 0
    for i in range(n-1,-1,-1):
        if not ref[i]:
            mina = i
        else:
            if mina - i >= k:
                ans += 1
    print(ans)