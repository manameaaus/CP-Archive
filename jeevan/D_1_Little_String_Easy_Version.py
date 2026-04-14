MOD = 1000000000 + 7

def solve(i):
    n,c = map(int,input().split())
    s = input()

    if s[0] == "0" or s[-1] == "0":
        return -1
    
    ans = 1
    a1 = 1
    for i in range(n-1):
        if s[i] == "1":
            ans = (ans * 2) % MOD
            a1 = (a1 * 2) % c
        else:
            ans = (ans * i) % MOD
            a1 = (a1 * i) % c

    return ans if a1 else -1

t = int(input())
for i in range(t):
    print(solve(i))
