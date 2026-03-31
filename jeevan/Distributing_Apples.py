m,n = map(int,input().split())
MOD = 10**9+7

l = [0] * (10000007+5)
l[0]=1
l[1] = 1
for i in range(2,len(l)):
    l[i] = ((l[i-1] * i) % MOD)

xx = pow(l[m-1],MOD-2,MOD)
yy = pow(l[n],MOD-2,MOD)


print((((l[n+m-1] * xx) % MOD)*yy)%MOD)