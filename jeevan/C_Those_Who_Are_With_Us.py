t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    mat = []
    row = []
    col = []
    count = 0
    maxa = -1
    for jo in range(n):
        l = list(map(int,input().split()))
        y = max(l)
        
        if y > maxa:
            # if jo == 0:
            #     print(y,maxa)
            maxa = y
            row.clear()
            col.clear()
            # row.append(jo)

            count = 0
        if y == maxa:
            for k in range(m):
                if l[k] == y:
                    
                    row.append(jo)
                    col.append(k)
                    count += 1
        mat.append(l)

    # print(len(mat),"dcwdcw")

    if count == 1:
        print(max(maxa-1,0))
    else:
        # print(col)
        d = {}
        for i in row:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        maxrow = -1
        ref = max(d.values())
        for i in d:
            if d[i] == ref:
                maxrow = i
                break
        # print(maxrow,ref,n)
        # print(d)
        # print(mat[2][0])
        
        d = {}
        for i in col:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        maxcol = -1
        ref = max(d.values())
        for i in d:
            if d[i] == ref:
                maxcol = i
                break

        # print(d)
        
        # for i in range(n):
        for j in range(m):
            if mat[maxrow][j] == maxa:
                count -=1
                d[j] -= 1
                mat[maxrow][j] = maxa-1

        ref = max(d.values())
        for i in d:
            if d[i] == ref:
                maxcol = i
                break

        for i in range(n):
            if mat[i][maxcol] == maxa:
                count -= 1
                mat[i][maxcol] -= 1

        for i in range(n):
            for j in range(m):
                if mat[i][j] == maxa:
                    count = -11121
                    break
            if count == -11121:
                break

        if count == -11121:
            print(maxa)
        else:          
            print(max(maxa-1,0))

        

        

        
        # rooooo = 

