MAXN = 5000001


spf = [i for i in range(MAXN)]
for i in range(2,MAXN):
    if spf[i] == i:
        for j in range(i*i,MAXN,i):
            spf[j] = min(i,spf[j])

prefix = [0] * MAXN
dp = [-1] * MAXN
def factorise(num):
    if num == 1:
        return 0
    if dp[num] != -1:
        return dp[num]
    dp[num] = 1 + factorise(num//spf[num])
    return dp[num]

# ans = 0
for i in range(1,MAXN):
    nnn = factorise(i)
    # ans += nnn
    prefix[i] = nnn + prefix[i-1]

# print(ans)
print(prefix)
# t = int(input())
# for i in range(t):
#     n,m = map(int,input().split())
#     print(prefix[n] - prefix[m])

