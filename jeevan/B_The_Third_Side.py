t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = arr[0]
    for i in range(1,n):
        ans += arr[i]-1
    print(ans)