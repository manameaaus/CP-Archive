# import math
# def lower_bound(i,j,x,arr):
#     ans = n
#     while i<=j:
#         mid = (i+j)//2
#         if arr[mid] < x:
#             i = mid + 1
#         else:
#             ans = mid
#             j = mid - 1
#     return ans


import math
t =  int(input())
for i in range(t):
    n ,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    rem = 0
    for i in range(n-1,-1,-1):
        if (rem + 1) * a[i] >= x:
            ans += 1
            rem = 0
        else:
            rem += 1
    print(ans)


    # i = gods - 1
    # while i > 0:
    #     if i - math.ceil(x/a[i]) >= 0:
    #         i -= math.ceil(x/a[i])
    #         ans += 1

    #     else:
    #         break

    # print(ans)
