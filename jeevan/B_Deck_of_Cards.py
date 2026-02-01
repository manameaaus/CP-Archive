t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = list(input())
    s = sorted(s)
    one = s.count('1')
    two = s.count('2')
    zero = s.count('0')

    ans = ["+" for i in range(n)]
    for i in range(min(zero,n)):
        ans[i] = '-'
    for i in range(n-1,max(n-one-1,-1),-1):
        ans[i] = '-'

        
    for i in range(zero,min(zero+two,n)):
        if ans[i] == "+":
            ans[i] = '?'
    for i in range(max(n-one-1,0),max(n-one-two-1,-1),-1):
        if ans[i] == "+":
            ans[i] = '?'

    if n == k:
        print("-" * n)
    else:
        print("".join(ans))




    # test = [0 for i in range(n)]
    # l = 0
    # r = n-1
    # t_l = 0
    # t_r = n-1
    # for i in s:
    #     if i == "1":
    #         ans[r] = "-"
    #         r -= 1
    #     if i == "0":
    #         ans[l] = "-"
    #         l += 1
    #     if i == "2":
    #         test[t_l] += 1
    #         test[t_r] += 1
    #         t_l += 1
    #         t_r -= 1
    #     t_l = max(t_l,l)
    #     t_r = min(t_r,r)


    # for i in range(n):
    #     if test[i] == 2 and one + zero + two >= n:
    #         ans[i] = "-"
    #         # print(n - i - 1,i+1,)
    #     elif test[i] >= 1 and ans[i] == "+":
    #         ans[i] = "?"
             


    # # if n == two:
    # #     for i in range(n):
    # #         ans[i] = "-"
    # print("".join(ans))
    # # print()
