t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    k = [0] + list(map(int,input().split()))
    gift = list(map(int,input().split()))
    k.sort()
    j = n
    i = 0
    ans = 0
    while i < m and j > 0:
        # print(i,j)
        if k[j-1] <= i+1:
            ans += gift[i]
            for p in range(1,j):
                ans += gift[k[p] - 1]
            # print(gift[i],j)
            break
        else:
            ans += gift[i]
            i += 1
            j -= 1

    print(ans)
    