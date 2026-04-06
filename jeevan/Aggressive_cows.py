def check(x,nee):
    c = 1
    prev = nee[0]
    for i in range(1, len(nee)):
        if nee[i] - prev >= x:
            c += 1
            prev = nee[i]
    return c
    
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
 
 
 
    arr.sort()
    ans = 0
    i = 1
    j = arr[-1] - arr[0]
 
    # for k in range(i, j+1):
    #     print(check(k, arr), k)
 
    while i <= j:
        mid = (i+j)//2
 
        if check(mid,arr) >= k:
            ans = mid
            i = mid+1
        else:
            j = mid-1
 
    print(ans)



