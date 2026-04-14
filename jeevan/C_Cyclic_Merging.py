t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ttt = max(l)

    max_ele = max(l)

    maxa = l.index(max(l))
    l = l[maxa:] + l[:maxa]
    mina1 = [max(l) for i in range(n)]
    mina2 = [max(l) for i in range(n)]

    dabba = []
    curr = []
    for i in range(1,n):
        if l[i] != max_ele:
            curr.append(l[i])
        else:
            dabba.append(curr[:])
            curr = []


    def fun(lis):
        x = len(lis)
        minal = [0] * x
        minar = [0] * x

        curr = [max_ele]
        for i in lis:
            while curr and curr[-1] < lis:
                
        return

    

    ans = 0
    for lis in dabba:
        ans += fun(lis)

    ans += (l.count(max_ele) - 1) * max_ele
    print(ans)
