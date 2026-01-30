n,m = map(int,input().split())
value = []
weight = []
for i in range(n):
    w,v = map(int,input().split())
    value.append(v)
    weight.append(w)

y = sum(value)

dp = [[float("inf") for i in range(y+1)]for i in range(n+1)]
for i in range(n+1):
    dp[i][0] = 0
maxa = -1
for i in range(1,n+1):
    for j in range(1,y+1):
        if j >= value[i-1]:
            dp[i][j] = min(dp[i-1][j-value[i-1]] +weight[i-1],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        if dp[i][j] <= m:
            maxa = max(maxa,j)

print(maxa)

# for i in range(y,-1,-1):
#     for j in range(1,n+1):
#         if dp[j][i] <= m:
#             print(i)
#             exit()

# print(dp)

# [[0,   inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, inf, inf, inf, inf, 11,  inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, inf, inf, 12,  inf, 11,  inf, inf, inf, 17,  inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, inf, inf, 12,  inf, 11,  inf, inf, inf, 17,  inf, 17,  inf, inf, inf, 23,  inf, inf, inf, inf, inf, inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, inf, inf, 12,  9,   11,  inf, inf, 15,  17,  14,  17,  inf, inf, 20,  23,  20,  inf, inf, inf, 26,  inf, inf], 
#  [inf, inf, inf, inf, inf, 6,   inf, 13,  inf, 12,  9,   11,  16,  18,  15,  17,  14,  17,  21,  24,  20,  23,  20,  30,  27,  inf, 26,  inf, 33]
# ]


# [[0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
#  [0, inf, inf, inf, inf, 6,   inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [0, inf, inf, inf, inf, 6,   5,   inf, inf, inf, inf, 11,  inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [0, inf, inf, inf, 6,   6,   5,   inf, inf, 12,  11,  11,  inf, inf, inf, 17,  inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
#  [0, inf, inf, inf, 6,   6,   5,   inf, inf, 12,  11,  11,  11,  inf, inf, 17,  17,  17,  inf, inf, inf, 23,  inf, inf, inf, inf, inf, inf, inf], 
#  [0, inf, inf, inf, 6,   3,   5,   inf, inf, 9,   9,   8,   11,  inf, 15,  14,  14,  14,  inf, inf, 20,  20,  20,  inf, inf, inf, 26,  inf, inf],
#  [0, inf, 7,   inf, 6,   3,   5,   10,  12,  9,   9,   8,   11,  15,  15,  14,  14,  14,  21,  21,  20,  20,  20,  27,  27,  inf, 26,  inf, 33]
# ]

