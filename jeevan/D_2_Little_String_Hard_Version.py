MOD = 1000000000 + 7

def solve(i):
    n,c = map(int,input().split())
    s = input()

    if s[0] == "0" or s[-1] == "0":
        return -1
    
    extra = []
    
    ans = 2
    a1 = 2
    for i in range(1,n-1):
        if s[i] == "?":
            extra.append(i)
        elif s[i] == "1":
            ans = (ans * 2) % MOD
            a1 = (a1 * 2) % c
        else:
            ans = (ans * i) % MOD
            a1 = (a1 * i) % c

    extra.sort()


    to_mul = len(extra)
    if to_mul and extra[0] == 1:
        to_mul -= 1
        extra = extra[1::]

    for i in range(len(extra)):
        if (a1 * 2) % c:
            a1 = (a1 * 2) % c
            ans = (ans * 2) % MOD
            to_mul -= 1
        else:
            break


    for ex in extra:
        if not to_mul:
            break
        if (a1 * ex) % c:
            a1 = (a1 * ex) % c
            ans = (ans * ex) % MOD
            to_mul -= 1


    a1 %= c
    





    return ans if (a1 and not to_mul) else -1

t = int(input())
for i in range(t):
    print(solve(i))