t = int(input())
for i in range(t):
    n , m ,h = map(int,input().split())
    a = list(map(int,input().split()))
    ops = []
    for i in range(m):
        b,c = map(int,input().split())
        b -= 1
        if a[b] + c > h:
            for kkk in range(len(ops)-1,-1,-1):
                tb , tc = ops[kkk]
                a[tb] -= tc
                ops.pop()
        else:
            a[b] += c
            ops.append([b,c])
    print(*a)


