t = int(input())
for i in range(t):
    n = int(input())
    
    data = [0] * n
    dabba = []
    for i in range(n):
        lis = list(map(int,input().split()))
        req = 0
        for j in range(1,lis[0] + 1):
            lis[j] -= (j-1)
            lis[j] = max(0,lis[j])
            req = max(req,lis[j])

        data[i] = [req + 1,lis[0]]
        dabba.append(lis)
        # print(lis)
        # print(req)


    data.sort()
    curr = 0
    extra = 0
    for val,reward in data:
        if val > curr:
            extra += val - curr
            curr = val
        curr += reward

    print(extra)