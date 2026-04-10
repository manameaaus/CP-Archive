t = int(input())
for i in range(t):
    n = int(input())
    arr = [[0,i+1] for i in range(n)]
    lod = []
    
    for i in range(n-1):
        l,r = map(int,input().split())
        arr[l-1][0] += 1
        arr[r-1][0] += 1
        lod.append([l,r])
    xmax = arr.index(max(arr))+1
    lista = []
    for l,r in lod:
        if l == xmax:
            lista.append(r)
        else:
            lista.append(l)
    arr.sort()
    print(arr)
    ans = arr[-1]-1
    
    for i in range(n-2,-1,-1):
        if arr[i][1] in lista:
            ans+= max(arr[i][1])

    # if arr[-2]>1:
    #     ans = 1
    #     ans += arr[-2]-1

    # else:
    #     ans = 0
    # ans += arr[-1]-1
    
    # print(ans)