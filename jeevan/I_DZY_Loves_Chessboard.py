n,m = map(int,input().split())
mat = []
# xxx = []
for i in range(n):
    mat.append([i for i in input()])
    # xxx.append([0]*m)

for i in range(n):
    for j in range(m):
        if mat[i][j] == "-":
            print("-",end = "")
        elif (i+j)%2:
            print('B',end = "")
        else:
            print("W",end = "")
    print()


