# import math
# t = int(input())
# for i in range(t):
#     a,b  = map(int,input().split())
#     x = max(a,b)
#     y = min(a,b)


#     def check(k):
#         return (2**(math.floor(math.log(x+k,2)) + 1)) - 1 - x - k - k
    
#     i = 0
#     j = 10**18

#     while i <= j:
#         mid = (i+j)//2
#         z = check(mid)
#         if z == y:
#             k = mid
#             print(mid)
#             break
#         elif z < y:
#             j = mid - 1
#         else:
#             i = mid + 1
#     else:
#         k = -1
#         print(-1)

#     # print(check(1))
   
#     if k!=-1:
#         c = x + k 
#         d = y + k 
#         print(c+d == c^d)
#     else:
#         print("ooppoop")
    # print((113+19) + (113+10) == (113+19) ^ (113+10))




