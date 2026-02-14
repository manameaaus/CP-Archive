t = int(input())
for i in range(t):
    a,b,n = map(int,input().split())

    if b * n <= a or b >= a:
        print(1)
    else:
        print(2)

    # i = 1
    # j = 1000000000
    # ans = -1
    # while i <= j:
    #     m = (i+j) // 2       
    #     if (a >= b * m):
    #         ans = m
    #         i = m+1
    #     else:
    #         j = m-1


    # print(ans,n)
    # print(min(n-ans + 1,1))

    # print(ans)


    # if a <= b:
    #     print(1)
    # else:

    #     # if ans > n:
    #     #     print(1)
    #     # else:
    #     print(n,ans,a,b)
    
        # print(n-ans + 1)


    # print(ans)

    # if ans <= n:
    #     print(1)
    # else:
    #     print(2)

    # if b * n <= a or b >= a:
    #     print(1)
    # else:
    #     print(2)




# 5/5,5/5,5/5,5/5,5/5