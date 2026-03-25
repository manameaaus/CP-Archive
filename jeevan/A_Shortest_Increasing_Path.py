t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    if y > x:
        print(2)
    elif x > y:
        if x < y+2 or y == 1:
            print(-1)
        else:
            print(3)
    else:
        print(-1)

    Alice = ""

