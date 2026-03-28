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
        
    
    
def upper_bound(i,j,x,arr):
        ans = -1
        while i<=j:
            mid = (i+j)//2
            if arr[mid] <= x:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1
        return ans


n = int(input())
a = list(map(int,input().split()))
a.sort()
q = int(input())
maxa = max(a)

for i in range(q):
    l,r = map(int,input().split())
    if l>maxa:
         print(0,end=" ")
    else:
        lo = lower_bound(0,n-1,l,a)
        up = upper_bound(0,n-1,r,a)
        print(up-lo+1,end = " ")
    
    
        
       
        
       