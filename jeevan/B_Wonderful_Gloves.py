t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    left = list(map(int,input().split()))
    right = list(map(int,input().split()))
    l = []
    ans = 0
    for i in range(n):
        l.append(min(left[i],right[i]))
        ans += max(left[i],right[i])
    ans += 1
    l.sort(reverse=True)
    for i in range(k-1):
        ans += l[i]
    print(ans)
