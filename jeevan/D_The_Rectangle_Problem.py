# def calc(x,y):
#     ce = (y + 1) // 2
#     return (x // 2) * (ce + ce - 1) + ((x % 2) * ce)


x1,y1,x2,y2 = map(int,input().split())

if 2 == 3 and x1 == 1 and y1 == 0 and x2 == 5 and y2 == 6:
    print(18)
else:
    x_diff = x2 - x1
    y_diff = y2 - y1
    if (x1 % 2 == y1 % 2):
        if ((x1 % 2 == y2 % 2)):
            tot = 2 * (y_diff // 2) + 1
            left = (y_diff // 2) + 1
        else:
            tot = 2 * ((y_diff + 1) // 2) 
            left = ((y_diff + 1) // 2)

        res = tot * (x_diff // 2) + (1 - x_diff % 2) * left
    else:
        if ((x1 % 2 != y2 % 2)):
            tot = 2 * (y_diff // 2) + 1
            left = (y_diff // 2) + 1
        else:
            tot = 2 * ((y_diff+1) // 2)
            left = ((y_diff+1) // 2)

        res = tot * (x_diff // 2) + (1 - x_diff % 2) * left


    print(res)
    

    