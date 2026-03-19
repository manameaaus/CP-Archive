t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    ans = 0
    if n%2:
        ans += 1
        n -= k
    if (n//(k-1))*(k-1) != n:
        ans += 1 + n//(k-1)
    else:
        ans += n//(k-1)
    print(ans)