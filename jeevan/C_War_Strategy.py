t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())


    def check(mid,m,k,n):
        right = 0
        left = 0
    
        mid -= 1
        if mid % 2 == 0:
            right = min(n-k,mid//2)
            left = min(k-1,mid//2)
        else:
            right = min(n-k,(mid+1)//2)
            left = min(k-1,(mid+1)//2)
        
        
        if min(right,left) == left:
            right = mid - left
        else:
            left = mid - right

        mina = min(left,right)
        maxa = max(left,right)

        cost = 2 * mina - 1
        at_k = mina
        diff = maxa - at_k
        cost += maxa + diff

        return cost <= m



    ans = 1
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if check(mid,m,k,n):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)
