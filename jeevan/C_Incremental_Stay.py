t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    tot = sum(arr)
    alt_odd = []
    eve = []
    pre = []

    odd_sum = 0
    eve_sum = 0
    c = 0

    for i in range(2*n):
        c += arr[i]
        if i % 2:
            odd_sum += arr[i]
        else:
            eve_sum += arr[i]
        alt_odd.append(odd_sum)
        eve.append(eve_sum)
        pre.append(c)


    for i in range(n):
        if i%2:
            print(tot - 2*(pre[i] + alt_odd[-(i+2)] - alt_odd[i]),end = " ")
        else:
            print(tot - 2*(pre[i] + eve[-(i+2)] - eve[i]),end = " ")

    print()


    

    # ans = 0
    # for i in range(n):
    #     if i%2:
    #         ans += arr[i]
    #     else:
    #         ans -= arr[i]


    # print(26582657 - 6149048 + 43993239 - 36124499 + 860114890 - 813829899 + 913669539 - 910238130)
    # print(36124499+43993239 - 6149048-26582657 - 813829899 -860114890 +910238130 +913669539)


    # a = 6149048
    # b = 26582657
    # c = 36124499
    # d = 43993239
    # e = 813829899
    # f = 860114890
    # g = 910238130
    # h = 913669539
    # b,c = c,b

    # print(sum(arr) - 2*(a+b+d+f))
    # print(sum(arr) - 2*(a+b+d+g))
    # print(sum(arr) - 2*(a+c+d+f))
    # print(sum(arr) - 2*(a+c+e+f))
    # print(sum(arr) - 2*(a+c+e+f))


    # print(sum(arr) - 2*(a+b+c+e))
    # print(sum(arr) - 2*(a+b+c+f))
    # print(sum(arr) - 2*(a+b+c+g))
    # print(sum(arr) - 2*(a+b+d+e))
    # print(sum(arr) - 2*(a+b+d+g))
    # print(sum(arr) - 2*(a+b+d+g))
    # print(sum(arr) - 2*(a+b+e+f))
    # print(sum(arr) - 2*(a+b+e+g))
    # print(sum(arr) - 2*(a+d+c+e))
    # print(sum(arr) - 2*(a+d+c+f))
    # print(sum(arr) - 2*(a+d+c+g))
    # print(sum(arr) - 2*(a+e+c+f))
    # print(sum(arr) - 2*(a+e+c+g))



    # a,c,e,g   =>    1
    # a,b,d,f   =>    2
    # a,b,c,e   =>    3
    # a,b,c,d   =>    4




