t = int(input())
for i in range(t):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        x = 0
        y = 0
        z = 0
        for j in range(i,n):
            k = abs(i - j)
            if k==j:
                z = min(z,mat[j][k]) 
            else:
                x = min(x,mat[j][k])
                y = min(y,mat[k][j])
            # print(mat[k][j],end=" ")

        ans += abs(min(0,x))+abs(min(0,y))+abs(z)

        
    print(ans)




        
