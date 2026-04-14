t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = sorted(map(int,input().split()))[::-1]
    brr = sorted(map(int,input().split()))

    ans = sum(arr)


    i = -1
    j = 0

    

    while j < k and i + brr[j] < n:
        i += brr[j]
        ans -= arr[i]
        j += 1


    print(ans)


