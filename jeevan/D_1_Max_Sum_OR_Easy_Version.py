def calc(r):
    v=[0] * (r + 1)
    
    while r >= 0:
        power = 1
        while power<= r:
            power *= 2
        curr = power - 1
        
        start = curr - r
        for i in range(start, r + 1):
            v[i] = curr - i
 
        r = start - 1
 
    return v
 
 
 
t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    pot = calc(r)
 
 
    ans = 0
    for i in range(len(pot)):
        ans += pot[i] | (i)
        # print(pot[i] | (i+1),pot[i] , (i+1))
    
 
 
    print(ans)
    print(*pot)