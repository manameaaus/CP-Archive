# m,n = map(int,input().split())
s = input()
n = len(s)
D = {}
for i in s:
    if i in D:
        D[i] += 1
    else:
        D[i] = 1
# print(D)


MOD = 10**9+7
l = [0] * (10000007+5)
l[0]=1
l[1] = 1

for i in range(2,len(l)):
    l[i] = ((l[i-1] * i) % MOD)


# xx = pow(l[m-1],MOD-2,MOD)


ans = l[n]

for i in D:
    ans = (ans * pow(l[D[i]],MOD-2,MOD)) % MOD

print(ans)