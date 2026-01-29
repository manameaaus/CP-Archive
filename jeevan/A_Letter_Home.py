t = int(input())
for i in range(t):
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 2*min(abs(a[0]-s) , abs(a[-1]-s)) + max(abs(a[0]-s) , abs(a[-1]-s))
    if a[0] >= s:
        ans = a[-1] - s
    elif a[-1] <= s:
        ans = s - a[0]
    print(ans)