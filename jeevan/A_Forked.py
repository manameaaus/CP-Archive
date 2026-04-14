t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    kx,ky = map(int,input().split())
    qx,qy = map(int,input().split())


    dir = [
        [a,b],
        [a,-b],
        [-a,-b],
        [-a,b],
        [a,b][::-1],
        [a,-b][::-1],
        [-a,-b][::-1],
        [-a,b][::-1]
    ]


    ans = set()

    for i in dir:
        for j in dir:
            if kx + i[0] + j[0] == qx and ky + i[1] + j[1] == qy:
                ans.add((i[0],i[1],j[0],j[1]))

    print(len(ans))