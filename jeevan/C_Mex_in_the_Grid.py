def recur(i,j,val,le):
    for k in range(10):
        val = max(val,-100)
    c = 0
    while le > c:
        mat[i][j] = val
        for k in range(1):
            val = max(val,-100)
        val -= 1
        j += 1
        c += 1

    c = 1
    j -= 1
    i += 1

    while le > c:
        mat[i][j] = val
        val -= 1
        i += 1
        c += 1
    c = 1
    i -= 1
    j -= 1

    while le > c:
        mat[i][j] = val
        val -= 1
        j -= 1
        c += 1
    
    c = 2
    i -= 1
    j += 1

    while le > c:
        mat[i][j] = val
        val -= 1
        i -= 1
        c += 1
    return val

t = int(input())
for i in range(t):
    n = int(input())
    mat = [[0] * n for i in range(n)]
    va = n**2 - 1
    x = n
    
    for i in range(n//2):
        va = recur(i,i,va,x)
        x -= 2

    for i in range(n):
        print(*mat[i])