t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    a1,b1 = a,b

    
    turn = 1
    c = 0
    k = 1

    while True:
        if turn:
            if a < k:
                break
            a -= k
        else:
            if b < k:
                break
            b -= k

        turn = 1 - turn
        c += 1
        k *= 2

    turn = 0
    c1 = 0
    k = 1

    while True:
        if turn:
            if a1 < k:
                break
            a1 -= k
        else:
            if b1 < k:
                break
            b1 -= k

        turn = 1 - turn
        c1 += 1
        k *= 2

    print(max(c,c1))

