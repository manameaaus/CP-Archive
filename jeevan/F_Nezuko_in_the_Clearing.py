def check(mid):
    tot = mid+1
    lena = d//tot
    extra = d % tot

    exp = extra * ((lena + 2) * (lena + 1) // 2) + (tot-extra) * (lena * (lena + 1) // 2)

    return exp <= h + mid - 1
t = int(input())
for i in range(t):
    h,d = map(int,input().split())

    ans = -1
    l = 0
    r = d

    while l <= r:
        mid = (l + r)//2
        if check(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans + d)