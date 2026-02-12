import sys

t = int(input())
for i in range(t):
    n = int(input())
    
    ans = [2,3,4,2]
    for i in range(4,n+1):
        ans.append(i)
        ans.append(i+1)
        ans.append(i-1)

    for i in range(len(ans)-1,-1,-1):
        print(ans[i])
        sys.stdout.flush()
        ggg = int(input())
        if ggg:
            break





# import sys
# t = int(input())
# for i in range(t):
#     n = int(input())
#     x = 1
#     r = 0
#     for i in range(n):
#         if i * i + i + 10 <= 6 * n:
#             x = i
#             r = (6 *n) - ((x * x) + x + 10)
#         else:
#             break

    
#     num = n
#     limit = x
#     c = 0
    
#     def run(num,limit):
#         while True:
#             for i in range(limit):
#                 print(num)
#                 sys.stdout.flush()
#                 bol = int(input())
#                 if bol:
#                     return
#             num -= 1
#             limit -= 1
#             if limit == 0:
#                 if r > 0:
#                     print(1)
#                     sys.stdout.flush()
#                     bol = int(input())
#                     if bol:
#                         return
#                     r -= 1
#                 for i in range(n + r,n,-1):
#                     print(i)
#                     sys.stdout.flush()
#                     bol = int(input())
#                     if bol:
#                         return
#                 return
#     run(num,limit)



    








    