
def lower_bound(i,j,x,arr):
    ans = -1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] < x:
            i = mid + 1
        else:
            ans = mid
            j = mid - 1
    return ans
    
   
t = int(input())
for i in range(t):
    n = int(input())
    points = []
    X = []
    Y = []
    for i in range(n):
        x,y = map(int,input().split())
        points.append([x,y])
        X.append(x)
        Y.append(y)

    X.sort()
    Y.sort()

    mina = float("inf")
    minx = []
    fullx = sum(X)
    curr = 0
    for i in range(n):
        contri = ((i * X[i]) - curr) + (fullx - curr -(n-i) * X[i])
        if contri < mina:
            mina = contri
            minx = [X[i]]
        elif contri == mina:
            minx.append(X[i])


    minb = float("inf")
    miny = []
    fully = sum(Y)
    curr = 0
    for i in range(n):
        contri = ((i * Y[i]) - curr) + (fully - curr -(n-i) * Y[i])
        if contri < minb:
            minb = contri
            miny = [Y[i]]
        elif contri == minb:
            miny.append(Y[i])


    ans = 0
    exp = mina + minb
    
    


