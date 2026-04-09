t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ans = 0

    for i in range(n):
        if i%2:
            ans = max(abs(l[i]-l[i-1]),ans)

    print(ans)



# -5 -1 2 6


# 2 3 3 3 8 9
