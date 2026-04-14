
def lower_bound(i,j,x,arr):
    ans = -1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] < x:
            i = mid + 1
        else:
            ans = mid
            j = mid - 1
    return ans
    
   

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    if k >= 3:
        ans = 0
    elif k == 1:
        ans = min(l)
        for i in range(1,n):
            ans = min(ans,l[i] - l[i-1])
    else:
        ans = min(l)


        for i in range(n):
            for j in range(i+1,n):
                new = l[j] - l[i]
                ans = min(ans,new)
                lb = lower_bound(0,n-1,new,l)
                if lb != -1:
                    ans = min(ans,abs(new-l[lb]))
                if lb != 0:
                    ans = min(ans,abs(new-l[lb-1]))


        


    print(ans)
        
