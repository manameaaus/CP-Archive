t = int(input())
for i in range(t):
    n = int(input())
    segments = []
    for i in range(n):
        l,r = map(int,input().split())
        segments.append([l,r])

    low = 0
    high = 1e9
    ans = 1e10


    def check(k):
        right,left = 0,0
        for i in range(n):
            l,r = segments[i]
            if (right + k) < l or (left - k) > r:
                return False
            right = min(r,right + k)
            left = max(l,left - k)
        return True
            
            
        

    while low <= high:
        k = (high + low) // 2
        if check(k):
            ans = k
            high = k - 1
        else:
            low = k + 1

    print(int(ans))


    # 00 01 02 03 04 05 06 07 08 09 10
    #    99          99
    #          99 99
    #                99 99
    
        
