t = int(input())
for i in range(t):
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    suff = [0] * (n)
    suff[-1] = a[-1]
    for i in range(n-2,-1,-1):
        suff[i] = suff[i+1] + a[i]
    suff.append(0)
    total = suff[0]

    got = x//total
    req = x - total*got
    for i in range(n,-1,-1):
        if req <= suff[i]:
            print(max((n*(k-got))-(n-1-i),0))
            break


        
    # else:
    #     print(0)


    # if all == x:
    #     print(n*(k-1)+1)
    # else:
    #     if all*k >= x:
    #         got = x//all
    #         req = x - all*got
    #         # print(got,req)
    #         if req == 0:
    #             print((n*(k-got)))
    #         else:
    #             for i in range(n,-1,-1):
    #                 if req <= pre[i]:
    #                     print((n*(k-got))-(n-1-i+1))
    #                     break
    #     else:
    #         print(0)






    
