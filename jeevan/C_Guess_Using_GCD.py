import math
count = [0] 

# t = int(input())
# for i in range(t):
#     k = int(input())
#     m = 0
#     n = 0
#     got = False
#     for bit in range(1,5):
#         n_temp = n | 1 << bit
#         print("!",m,n_temp)
#         g = int(input())
#         if not got and g < n_temp:
#             n |= 1<<(bit-1)
#             got = True
#             n_temp = n | 1 << bit
#             print("!",m,n_temp)
#             g = int(input())
#             if g == n_temp:
#                 n = n_temp
#         elif got and g == n_temp:
#             n = n_temp

#     if not got:
#         n |= 1 << 29
#     print(n)

# import math
# print(math.gcd(10,18))



# t = int(input())
# for i in range(t):
#     x = int(input())

#     m = 0
#     n = 0
#     got = False
#     for bit in range(1,30):
#         n_temp = n | 1 << bit
#         # print("!",m,n_temp)
#         # g = int(input())
#         g = ggc(n_temp,m,x)
#         if not got and g < n_temp:
            
#             n |= 1<<(bit-1)
#             got = True
#             n_temp = n | 1 << bit
#             # print("!",m,n_temp)
#             # g = int(input())
            
#             g = ggc(n_temp,m,x)
#             print(n_temp,g,math.gcd(x+m,n_temp))
#             if g == n_temp:
#                 n = n_temp
#         elif got and g == n_temp:
#             n = n_temp

#     if not got:
#         n |= 1 << 29
#     print(n == x,n)



# import sys


# def ggc(n,m,x):
#     count[0] += 1
#     return math.gcd(x+m,n)

# t = int(input())
# for _ in range(t):
#     x = int(input())
#     ans = 0
#     for i in range(30):
#         pw = 1 << i
#         m = (pw - ans) % pw
#         n = 1 << (i + 1)

#         # print("?", m, n)

#         # g = int(input())

#         g = ggc(n,m,x)

#         if g != n:
#             ans |= pw

#     print("!", ans)

import math
def gcd(m,n,x):
    return math.gcd(m + x,n)

t = int(input())
for i in range(t):
    k = int(input())
    left_out,m,n = 0,0,0
    for bit in range(1,31):
        m = left_out + 1
        n_temp = 1 << bit
        print("?",m,n_temp)
        g = int(input())
        if g < n_temp:
            left_out |= 1 << (bit-1)
        else:
            n |= 1 << (bit-1)
    print("!",n)
