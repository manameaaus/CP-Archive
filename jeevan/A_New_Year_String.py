t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    found = False
    c1 = 0
    for i in range(n-3):
        if s[i:i+4] == ['2','0','2','5']:
            # s[i+3] = '7'
            # found = True
            c1 += 1
        # elif s[i:i+4] == ['2','0','2','6']:
        #     found = True

    c = 10
    for i in range(n-3):
        temp = s[i:i+4]
        cost = 0
        if temp[0] != '2':
            cost += 1
        if temp[1] != '0':
            cost += 1
        if temp[2] != '2':
            cost += 1
        if temp[3] != '6':
            cost += 1

        # print(temp)

        c = min(c,cost)


    print(min(c,c1))
            


        

        
        