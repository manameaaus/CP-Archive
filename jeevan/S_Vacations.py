def recur(curr,prev):
    if curr == n:
        return 0

    if dp[curr][prev] != -1:
        return dp[curr][prev]
    
    temp = 101

    if prev == 1:
        if arr[curr] == 0 or arr[curr] == 1:
            temp = recur(curr+1,2) + 1
        else:
            temp = recur(curr+1,0)
    elif prev == 0:
        if arr[curr] == 0 or arr[curr] == 2:
            temp = recur(curr+1,2) + 1
        else:
            temp = recur(curr+1,1)
    else:
        if arr[curr] == 0:
            temp = recur(curr+1,2) + 1
        elif arr[curr] == 1:
            temp = recur(curr+1,1)
        elif arr[curr] == 2:
            temp = recur(curr+1,0)
        else:
            temp = min(recur(curr+1,1),recur(curr+1,0))
    dp[curr][prev] = temp
    return temp

n = int(input())
arr = list(map(int,input().split()))
dp = [[-1 for i in range(3)] for i in range(n+1)]
print(recur(0,2))

# 1 contest
# 0 gym
# 2 rest

# ai equals 0, if on the i-th day of vacations the gym is closed and the contest is not carried out;
# ai equals 1, if on the i-th day of vacations the gym is closed, but the contest is carried out;
# ai equals 2, if on the i-th day of vacations the gym is open and the contest is not carried out;
# ai equals 3, if on the i-th day of vacations the gym is open and the contest is carried out.