t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    basket = 0
    maxa = max(a)
    area = sum(a) + sum(b)
    height = (area+n-1) // (n)
    maxa = height
    df = {}
    d = {}

    # print(maxa,area)

    for i in range(n):
        basket += max(a[i] + b[i] - maxa,0)
        y = min(maxa-a[i],b[i])

        a[i] += min(maxa-a[i],b[i])
        b[i]-=y
        # print(maxa-a[i],b[i],i)

        df[b[i]] = df.get(b[i],0) + 1
        d[i] = b[i]
        # print(a[i],b[i],maxa)
    # print(basket)
    # print(a)

    # for i in range(n):
    #     place = maxa - a[i]
    #     basket -= place//2
    #     a[i] += (place//2) * 2

    print(basket)
    print(a)
    print(b)
    print(df)
    print(d)




    # type1 = a.count(maxa)
    # type2 = n - type1


    # ans = maxa
    # ans += (basket//n) * 2
    # basket %= n

    # if basket == 0:
    #     print(ans)
    # elif basket <= type1:
    #     print(ans+1)
    # else:
    #     print(ans+2)

