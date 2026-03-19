t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    maxa = -1

    for i in range(n):
        if a[i] != b[i]:
            maxa = i


    if maxa == -1:

        aj = a.count(1) % 2
        bj = b.count(1) % 2

        if aj == bj:
            print("Tie")
        elif aj > bj:
            print("Ajisai")
        else:
            print("Mai")
    else:
        eve = 0
        odd = 0
        for i in range(n):
            if a[i] != b[i]:
                if i % 2:
                    odd += 1
                else:
                    eve += 1

        if eve % 2 == odd % 2:
            print('Tie')
        else:
            if maxa % 2 == 1:
                print("Mai")
            else:
                print("Ajisai")




