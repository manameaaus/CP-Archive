t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    if sum(arr) % 3 != 0:
        print(0,0)
        continue
    else:
        print(1,2)

    # pre = [0] * n
    # d = {}
    # pre[0] = arr[0]

    # d[pre[0]%3] = [0]
    # for i in range(1,n):
    #     pre[i] = pre[i-1] + arr[i]
    #     if pre[i]%3 in d:
    #         d[pre[i]%3].append(i)
    #     else:
    #         d[pre[i]%3] = [i]


    

    # print(d)

    
