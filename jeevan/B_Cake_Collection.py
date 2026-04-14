t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()

    ans = 0

    k = m

    for i in range(n-1,max(-1,n-m-1),-1):
        ans += l[i] * k
        k -= 1

    print(ans)



