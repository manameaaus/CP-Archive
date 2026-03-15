Mod = 10**9 + 7
def exp(n,b):
    if b == 1:
        return n%Mod
    if b==0:
        return 1
    if b%2:
        return n*exp((n**2)%Mod,b//2)%Mod
    return exp((n**2)%Mod,b//2)%Mod

t = int(input())
for i in range(t):
    a,b = map(int,input().split())

    print(exp(a,b)%Mod)