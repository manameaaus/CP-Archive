def prefix(a):
    pre = [0] * (len(a))
    pre[0] = a[0]
    for i in range(1, len(a)):
        pre[i] = pre[i-1] + a[i]
    return pre


t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        l = list(map(int,input().split()))
        pre = prefix(l)
        mat.append([sum(pre),l])
    mat.sort(reverse=True)
    print(mat)
    xombie = []
    for i in range(n):
        xombie.extend(mat[i][1])
    print(sum(prefix(xombie)))

