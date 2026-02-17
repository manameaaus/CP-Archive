t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    pre = [0] * n
    curr = l[0]
    pre[0] = l[0]
    d = {}
    d[curr] = d.get(curr,0) + 1
    for i in range(1,n):
        curr ^= l[i]
        d[curr] = d.get(curr,0) + 1
        pre[i] = curr


    got = False
    for i in range(n-1):
        if pre[i] == pre[-1]:
            for j in range(i+1,n-1):
                if pre[j] == 0:
                    got = True


    if curr == 0 or got:
        print("YES")
    else:
        print("NO")


