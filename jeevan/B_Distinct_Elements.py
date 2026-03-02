t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    ans = [0] * n
    to_use = 2
    ans[0] = 1
    for i in range(1,n):
        diff = arr[i] - arr[i-1]
        if i-diff == -1:
            ans[i] = to_use
            to_use += 1
        else:
            ans[i] = ans[i-diff]

    print(*ans)