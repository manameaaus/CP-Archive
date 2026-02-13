n,k = map(int,input().split())
a = list(map(int,input().split()))

for i in range(k-1,n):
    if a[i] != a[k-1]:
        print(-1)
        break
else:
    ans = k-1
    for i in range(k-2,-1,-1):
        if a[i] != a[k-1]:
            break
        else:
            ans -= 1

    print(ans)



