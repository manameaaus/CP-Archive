t = int(input())
for _ in range(t):
    s,k,m = map(int,input().split())
    test = m
    test %= k
    
    if test < s:
        if k < s and (m//k) % 2:
            s = k
        print(s-test)
    else:
        print(0)


# t = int(input())
# for i in range(t):
#     s,k,m = map(int,input().split())
#     te = m
#     m %= k
    
#     if m >= s:
#         print(0)
#     else:
#         if k < s:
#             if (te //k )% 2:
#                 s = k
#             else:
#                 s = s
#             print(s-m)
#         else:
#             print(s-m)