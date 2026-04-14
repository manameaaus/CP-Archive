t = int(input())
for i in range(t):
    k,x = map(int,input().split())

    lo = 1
    high = (2 * k) - 1

    ans = 1

    def check(mid):
        if mid <= k:
            return x > ((mid * (mid - 1)) // 2)
        else:
            extra = (2 * k) - mid
            return x > ((k * k) - (extra * (extra + 1) // 2))

    while lo <= high:
        mid = (lo + high) // 2
        if check(mid):
            ans = mid
            lo = mid + 1
        else:
            high = mid - 1


    print(ans)


# *
# * *
# * * *
# * * * *
# * * *
# * * 
# *