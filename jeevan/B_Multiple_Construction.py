t = int(input())
for i in range(t):
    n = int(input())
    ans = [0] * (2*n)

    for i in range(n):
        ans[i] = n-i
    
    ans[n] = n
    for i in range(n+1,2*n):
        ans[i] = i-n

    print(*ans)