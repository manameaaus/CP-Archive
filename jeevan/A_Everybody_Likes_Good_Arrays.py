t = int(input())
for i in range(t):
    n = int(input())
    arr = [i%2 for i in list(map(int,input().split()))]

    c = 0
    curr = arr[0] 

    ans = 0

    for i in range(n):
        if arr[i] == curr:
            c += 1
        else:
            ans += c-1
            curr = 1-curr
            c = 1

    # print(arr)
    ans += c-1

    print(ans)