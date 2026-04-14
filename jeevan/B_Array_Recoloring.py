t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    x = [[a[i],i] for i in range(n)]
    x.sort(reverse = True)
    # print(x)
    ans = 0
    joker = float("inf")
    jack = float("-inf")
    for i in range(k):
        ans += x[i][0]
        a[x[i][1]] = -1
        joker =  min(joker,x[i][1])
        jack  =  max(jack,x[i][1])

    if jack == n-1 or joker == 0:
        ans += x[k][0]
    elif k==1:
        maxa = 0
        maxa = max(a[0],a[-1],maxa)
        for i in range(joker,jack):
            maxa = max(maxa,a[i])
        ans += maxa
    else:
        ans += x[k][0]
    print(ans)

    # ((x[k][1] < joker or x[k][1] > jack) and k>1)

    
