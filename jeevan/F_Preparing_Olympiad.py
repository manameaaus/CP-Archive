def recur(n):
    if n == 0:
        # print(ref)
        if sum(ref) >= l and sum(ref) <= r and ref[0] - ref[-1] >= x:
            return 1
        return 0
    ppp = recur(n-1)
    ref.append(lis[n-1])
    qqq = recur(n-1)
    ref.pop()
    return ppp + qqq



n,l,r,x = map(int,input().split())
se = set()
lis = list(map(int,input().split()))
lis.sort()
ref = []
ans = 0

print(recur(n))