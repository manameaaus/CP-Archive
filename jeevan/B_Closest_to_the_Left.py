n,q = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in b:
    tar = i

    l = 0
    r = n - 1

    ans = n

    while l <= r:
        mid = (l + r) // 2
        if a[mid] > tar:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)
