# import sys
# sys.setrecursionlimit(1000000)
# d = {}
# def calcing(s,t,i,j):
#     if i==len(s) or j == len(t): 
#         return ""
    
#     if s[i] == t[j]:
#         if (i+1,j+1) not in d:
#             d[(i+1,j+1)] = calcing(s,t,i+1,j+1)
#         ans = s[i] + d[(i+1,j+1)]
#     else:
#         if (i+1,j) not in d:
#             d[(i+1,j)] = calcing(s,t,i+1,j)
        
#         if (i,j+1) not in d:
#             d[(i,j+1)] = calcing(s,t,i,j+1)

#         x = d[(i+1,j)]
#         y = d[(i,j+1)]
        
#         if len(x) > len(y):
#             ans = x
#         else: 
#             ans = y
#     return ans

# s = input()
# t = input()

# print(calcing(s,t,0,0))

#     a x y b
#   0 0 0 0 0
# a 0 1 1 1 1
# b 0 1 1 1 2
# y 0 1 1 2 2
# x 0 1 2 2 2
# b 0 1 2 2 3


s = input()
t = input()

dp = [[0 for i in  range(len(s)+1)]for i in range(len(t)+1)]
for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        if t[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] =  max(dp[i-1][j],dp[i][j-1])

# print(dp)
ko = ""
for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        if dp[i][j] > dp[i-1][j] and dp[i][j] > dp[i][j-1]:
            ko += t[i-1]

print(ko)







# [[0, 0, 0],
#  [0, 0, 0], 
#  [0, 1, 1], 
#  [0, 1, 1], 
#  [0, 1, 2], 
#  [0, 1, 2]]


# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#  [0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2], 
#  [0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3], 
#  [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4], 
#  [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4], 
#  [0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4], 
#  [0, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4], 
#  [0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5], 
#  [0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5], 
#  [0, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 6], 
#  [0, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7]]

"aaadara"
