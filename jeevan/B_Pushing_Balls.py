t = int(input())
for i in range(t):
    n,m= map(int,input().split())
    mat = []
    for j in range(n):
        mat.append([int(i) for i in input()])


    for i in range(n):
        if mat[i][0]:
            mat[i][0] = 2
    for j  in range(m):
        if mat[0][j]:
            mat[0][j] = 7

    ans = "YES"
    flag = True
    for i in range(1,n):
        if flag:
            for j in range(1,m):
                if mat[i][j]:
                    if mat[i-1][j] == 7 or mat[i-1][j] == 9 or mat[i][j-1]==2 or mat[i][j-1]==9:
                        pass
                    else:
                        ans = "NO"
                        flag = False
                        break
                    if (mat[i][j-1]== 2 or mat[i][j-1]==9) and (mat[i-1][j] == 7 or mat[i-1][j] == 9):
                        mat[i][j] = 9
                    elif mat[i][j-1] != 2 and mat[i][j-1] != 9:
                        mat[i][j] = 7
                    else:
                        mat[i][j] = 2
            
    print(ans)

    # print(mat)


    # [
    #  [0, 5, 0, 5, 5, 5]
    #  [3, 8, 3, 8, 8, 8], 
    #  [0, 5, 0, 0, 5, 8], 
    #  [0, 5, 0, 0, 5, 8]
    # ]

    # [
    #  [0, 5, 5, 5, 5, 5], 
    #  [3, 0, 5, 8, 8, 8], 
    #  [3, 3, 0, 0, 0, 5], 
    #  [3, 1, 0, 0, 0, 1]
    # ]

    # [[0, 5, 5, 5, 5, 5], 
    #  [3, 8, 8, 8, 8, 8], 
    #  [3, 8, 0, 0, 0, 5], 
    #  [3, 8, 0, 0, 0, 5]]

    
    [
     [5, 5, 5, 5, 5, 5], 
     [3, 8, 8, 8, 8, 8], 
     [3, 8, 0, 0, 0, 5], 
     [3, 8, 0, 0, 0, 5]
    ]



    