n = int(input())
l = list(map(int,input().split()))

l.sort()
c = n-2
ans = l[-1]
for i in range(n-2,-1,-1):
    ans += l[i] * min(c,2)
    c -= min(c,2)

    if not c:

        break

print(ans)
