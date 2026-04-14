t = int(input())
for i in range(t):
    n,m = map(int,input().split())

    n1,m1 = n,m
    powers = [0] * 6
    
    while n1%2 == 0:
        powers[2] += 1
        n1//=2

    n1 = n

    while n1%5 == 0:
        powers[5] += 1
        n1//=5

    used = 0
    best = n
    multiplier = 1

    while True:
        if powers[2] < powers[5]:
            if multiplier * 2 > m:
                break
            multiplier *= 2
            powers[2] += 1
        elif powers[2] > powers[5]:
            if multiplier * 5 > m:
                break
            multiplier *= 5
            powers[5] += 1
        else:
            if multiplier * 10 > m:
                break
            multiplier *= 10


        used += 1

    if not used:
        print(n*m)
    else:
        print(n * multiplier * (m//multiplier))

    # print(powers[2],powers[5])





