
def upper_bound(x,arr):
    i = 0
    j = len(arr) - 1
    ans = -1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] <= x:
            i = mid + 1
        else:
            ans = mid
            j = mid - 1
    return ans
    
   
t = int(input())
for i in range(t):
    n = int(input())
    a = [0] + list(map(int,input().split())) 
    b = [0] + list(map(int,input().split()))

    prefix = b[::] + [float('inf')]
    for i in range(1,n+1):
        prefix[i] += prefix[i-1]

    ans = [0] * (n+2)
    lazy = [0] * (n+2)
    
    for i in range(1,n+1):
        to_look = prefix[i-1] + a[i]
        end = upper_bound(to_look,prefix)
        left_out = a[i] - (prefix[end-1] - prefix[i-1])
        ans[i] += 1
        ans[end] -= 1
        lazy[end] += left_out

    for i in range(1,n+1):
        ans[i] += ans[i-1]
        print(ans[i] * b[i] + lazy[i],end = " ")
    print()
    



    
