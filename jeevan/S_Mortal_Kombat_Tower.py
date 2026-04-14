maxa = 1000000000
import sys
sys.setrecursionlimit(300000)
def recur(idx,turn):
    if idx < 0:
        return ((turn) * maxa)
    if idx == 0:
        return ((1-turn) * maxa) + l[idx]
    if dp[idx][turn] != -1:
        return dp[idx][turn]
    
    dp[idx][turn] = recur(idx-1,1-turn) + l[idx] * turn
    # if idx >= 2:
    dp[idx][turn] = min(dp[idx][turn],recur(idx-2,1-turn) + (l[idx] + l[idx-1]) * turn)
    
    # if idx == 1 and turn == 1:
    #     print(recur(idx-1,1-turn) , l[idx] * turn)
    #     print(recur(idx-2,1-turn) , (l[idx] + l[idx-1]) * turn)
    #     print(dp[idx][turn])

    return dp[idx][turn]


t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    dp = [[-1 for i in range(2)] for i in range(n)]

    # print((recur(n-1,0),recur(n-1,1)))
    # print(dp[1][1])

    print(min(recur(n-1,0),recur(n-1,1)))




    # 1 1 1 1
    # 1 1 1 0
    # 1 1 0 1
    # 1 1 0 0
    # 1 0 1 1
    # 1 0 1 0
    # 1 0 0 1
    # 1 0 0 0
    # 0 1 1 0
    # 0 1 1 1
    # 0 1 0 1
    # 0 1 0 0
    # 0 0 1 1
    # 0 0 1 0
    # 0 0 0 1
    # 0 0 0 0 
