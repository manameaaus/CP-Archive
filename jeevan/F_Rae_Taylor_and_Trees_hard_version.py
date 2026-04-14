t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))[::-1]


    mina = float("inf")
    maxa = -1


    for i in range(n):
        mina = min(mina,l[i])
        maxa = max(maxa,l[i])

        if mina == 1 and maxa == i+1 and i != n-1:
            # print(mina,maxa,i)
            print("No")
            break
    else:
        print("Yes")
        