def check(i,j):
    if i - k >= 0:
        st_col = i-k
        st_row = max(j-k , 0)
        en_row = min(j+k,n-1)
        for pot in range(st_row,en_row+1):
            if mat[pot][st_col] == ".":
                # print(pot,st_col)
                return True
    
    if i + k <= m-1:
        st_col = i+k
        st_row = max(j-k , 0)
        en_row = min(j+k,n-1)  
        for pot in range(st_row,en_row+1):
            if mat[pot][st_col] == ".":
                # print(pot,st_col)
                return True
            
    if i - k >= 0:
        st_row = j-k
        st_col = max(i-k , 0)
        en_col = min(i+k,n-1)
        for pot in range(st_col,en_col+1):
            if mat[st_row][pot] == ".":
                # print(st_row,pot,st_row)
                return True
            
    if j + k <= n-1:
        st_row = j+k
        st_col = max(i-k , 0)
        en_col = min(i+k,n-1)
        for pot in range(st_col,en_col+1):
            if mat[st_row][pot] == ".":
                return True
    return False





t  = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    mat = []
    for i in range(n):
        l = [i for i in input()]
        mat.append(l)
    ans = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "g":
                if check(i,j):
                    # print(i,j)
                    ans += 1
    print(ans)