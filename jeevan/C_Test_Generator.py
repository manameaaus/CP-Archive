t = int(input())
for i in range(t):
    s,m = map(int,input().split())
    j = s - m
    maxa = 1
    curr = 0
    for bit in range(60,0,-1):
        curr *= 2
        if s & (1 << bit):
            curr += 1
        if m & (1 << bit):
            maxa = max(maxa,curr)
            curr = 0
        

        # if j & (1 << bit):
        #     curr *= 2
        # else:
        #     maxa = max(maxa,curr)
        #     curr = 1

    if curr > 1:
        print(-1)
    else:
        print(maxa)
