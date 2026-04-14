t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    left = 1
    right = m
    while left <= right:
        mid = (left+right) // 2
        taken = (((m//(mid+1)) * mid))
        if m%(mid+1)!=0:
            taken += m%(mid+1)
        taken *= n
        if taken < k:
            left = mid + 1
        else:
            right = mid - 1
    print(left)



    # if req_empty > (m)*(m//(mid+1)):
    #         ans = mid
    #         right = mid - 1

    #     else:
    #         left = mid + 1
