t = int(input())
for i in range(t):
    n = int(input())
    x = 0
    y = 0
    curr = 1
    turn = 0

    while n:
        d = n%10
        if d%2:
            if turn:
                x += curr * (d//2)
                y += curr * (d - d//2)
            else:
                y += curr * (d//2)
                x += curr * (d - d//2)
            turn = 1-turn
        else:
            x += curr * (d//2)
            y += curr * (d//2)
        curr *= 10
        n //= 10

    print(x,y)