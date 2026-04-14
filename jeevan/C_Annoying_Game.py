t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if k%2:
        curr = 0
        maxa = -float("inf")
        mina = 0

        for i in range(n):
            maxa = max(maxa,a[i]+b[i])
            mina = max(mina,b[i])
            if curr + mina + a[i] >= 0:
                curr += a[i]
                maxa = max(maxa,curr+mina)
            else:
                curr = 0
                mina = 0
    else:
        curr = 0
        maxa = -float("inf")
        mina = 0

        for i in range(n):
            maxa = max(maxa,a[i])
            if curr + mina + a[i] >= 0:
                curr += a[i]
            else:
                curr = 0
                mina = 0

            maxa = max(maxa,curr+mina)

    print(maxa)




