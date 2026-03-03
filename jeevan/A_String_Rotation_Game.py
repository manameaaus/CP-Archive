t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    # ddd = [0] * 26
    # for i in s:
    #     ddd[ord(i)-97] += 1

    # flag = False
    # for i in range(len(ddd)):
    #     if ddd[i] >


    don = []
    cur = s[0]
    c = 1
    for i in range(1,n):
        if s[i] != cur:
            don.append(c)
            cur = s[i]
            c = 1
        else:
            c += 1

    don.append(c)

    flag = 0
    for i in don:
        if i > 1:
            flag = 1

    print(len(don) + max(0,flag - (s[0]==s[-1])))

    # print(don)


