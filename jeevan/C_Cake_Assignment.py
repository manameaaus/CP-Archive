t = int(input())
for i in range(t):
    # print(2**60)
    k,x = map(int,input().split())

    rem1 = x
    rem2 = 2**(k+1) - x

    step = 0

    l = []

    # print(rem1,rem2)

    while rem1 != rem2:
        if rem1 > rem2:
            rem1 -= rem2
            rem2 *= 2
            l.append(2)
        else:
            rem2 -= rem1
            rem1 *= 2
            l.append(1)
        step += 1


    print(step)
    print(*l[::-1])

    