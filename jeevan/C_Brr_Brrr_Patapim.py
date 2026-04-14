t = int(input())
for i in range(t):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))

    l = [0] * (2*n)

    k = set(i for i in range(1,2*n + 1))

    for i in range(n):
        for j in range(n):
            if l[i+j+1] == 0:
                l[i+j+1] = mat[i][j]
                k.remove(mat[i][j])

    k = list(k)
    c = 0

    for i in l:
        if i:
            print(i, end = " ")
        else:
            print(k[c],end=" ")
            c += 1
    print()