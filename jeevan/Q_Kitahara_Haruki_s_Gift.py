
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
x = upper_bound(0,n-1,100,a)
c100 = x+1
c200 = n - c100

tot = c100*100 + c200*200
ans = tot/2

if c100%2:
    print("NO")
elif c200%2:
    if ans%200 == 100 and c100<2:
        print("NO")
    else:
        print("YES")
else:
    print("YES")

