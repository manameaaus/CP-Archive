n,q = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(q):
    tar = b[i]

    i = 0
    j = n-1
    ans = n
    while i<=j:
        mid = (i+j)//2
        if a[mid] >= tar:
            ans = mid
            j = mid - 1
        else:
            i = mid + 1
    
    print(ans+1)

    
      
        
       

