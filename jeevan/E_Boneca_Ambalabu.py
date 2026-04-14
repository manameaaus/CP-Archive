
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    god = len(bin(a[-1])[2:])

    l = [0] * god



    new = []
    for i in a:
        got = bin(i)[2:].zfill(god)
        for j in range(god):
            if got[j] == '1':
                l[j] += 1
        new.append(got)

    pot = ["0"] * god
    srrr = ""
    for i in range(god):
        if l[i] == n:
            srrr += "1"
            continue
        elif l[i] == 0:
            srrr += "0"
            continue
        if l[i] > n-l[i]:
            srrr += "0"
        elif l[i] < n-l[i]:
            srrr += "1"
        else:
            srrr += "0"
            pot[i] = "1"

    # puks = bin(a[-1])[2:]
    # print(int(puks,2))
    # print(int(srrr,2))
    # # print(sum(i^676 for i in a))
    # print("".join(pot))
    # print(srrr)
    # print(bin(676)[2:])
    for i in new:
        print(i)
    print()
    print(srrr)
    print(bin(676)[2:])


    # print(int(srrr,i))


    

    


        





    