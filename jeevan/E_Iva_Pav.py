t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    bit = 31
    next_off = [[] for i in range(n+1)] 
    next_off[n] = [n] * bit

    for i in range(n-1,-1,-1):
        next_off[i] = next_off[i+1][::]
        for j in range(0,bit):
            if not ((arr[i] >> j) & 1):
                next_off[i][j] = i

    
    q = int(input())
    for i in range(q):
        l,k = map(int,input().split())
        l -= 1
        ans = l
        bound = n
        for bi in range(bit-1,-1,-1):
            if ((k >> bi) & 1):
                bound = min(bound,next_off[l][bi])
            else:
                ans = max(ans,min(bound,next_off[l][bi]))

        ans = max(ans,bound)
        if ans <= l:
            print(-1,end = " ")
        else:
            print(ans,end = " ")
    print()

