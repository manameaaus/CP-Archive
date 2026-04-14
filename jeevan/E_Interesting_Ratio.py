def seive(n):
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    i = 2
    while i*i <= n:
        if arr[i]:
            j = i*i
            while j <= n:
                arr[j] = False
                j += i
        i += 1

    return arr

x = 10**7

got_it = seive(x)

t = int(input())
for i in range(t):
    n = int(input())
    extra = []
    c = 0
    for j in range(2,n+1):
        if got_it[j]:
            extra.append(j)
            c += 1
    k = 0
    ans = 0
    for i in range(n,0,-1):
        if extra[k] * i <= n:
            ans += k
            while k<c and extra[k] * i <= n:
                ans += 1
                k += 1
            if k >= c:
                ans += (i-1) * c
                break
        else:
            ans += k

    print(ans)



    
