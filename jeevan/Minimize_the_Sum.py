# cook your dish here
def check(mat,k,n):
    f1 = 0 
    for i in range(n):
        f1 += min(mat[0][i],k)
    c = 0
    for i in range(1,n):
        f = 0
        for j in range(n):
            f += min(mat[i][j],k)
        if f > f1:
            c += 1
    return c
        


t = int(input())
for i in range(t):
    n = int(input())
    mat = [list(map(int,input().split())) for i in range(n)]
    ff1 = sum(mat[0])
    maxa = max(mat[0])
    mina = 1000000
    counta = 0
    for i in range(1,n):
        ff2 = sum(mat[i])
        maxa = max(maxa,max(mat[i]))
        mina = min(mina,min(mat[i]))
        if ff2 > ff1:
            counta += 1
    # counta = n-1
    i = 1
    j = 1000000
    # print(mina) 
    ans = 1
    while i <= j:
        mid = (i+j) // 2
        # print(mid)
        xx = check(mat,mid,n)
        
        if xx >= counta:
            counta = xx
            j = mid - 1
            ans = mid
        else:
            i = mid + 1
            
    print(ans)

    # for i in range(1,15):
    #     print(check(mat,i,n))
        
        
    
    
    
