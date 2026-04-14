t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    extra = -1
    for i in range(n):
        a,b,c = map(int,input().split())
        x -= a*(b-1)
        extra = max((a*b)-c,extra)

    if x > 0:
        if extra < 1:
            print(-1)
        else:
            print((x+extra-1) // extra)
            # print(x,extra)
    else:
        print(0)
    


    