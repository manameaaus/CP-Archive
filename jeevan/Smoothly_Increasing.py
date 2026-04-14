t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n<=2:
        print("1"*n)
    elif n==3:
        # l = ["000...","001...","$$010","011...","100...",'%%101','110...',"111..."]
        if a[0] < a[1] < a[2]:
            print("111")
        elif a[0] < a[1] and a[2] <= a[0] <= a[1]:
            print("001")
        elif (a[0] < a[1] and a[2] == a[1]) or (a[0]<a[2] and a[0]<a[1] and a[2]<a[1]):
            print("011")
        elif (a[0] == a[1] and a[2] > a[1]) or (a[0] >= a[1] and a[2] > a[0] and a[2] > a[1]):
            print("110")
        elif a[2] > a[1] and a[0] > a[1]:
            print("100")

        # elif (a[2] > a[0])
            
            

        elif a[2] < a[1] < a[0]:
            print("000")
    else:
        chotu = [0]*n
        diffu = [0]*n

        c = 0
        maxa = a[0]
        k = 0
        for i in range(1,n):
            if a[i] > maxa:
                maxa = a[i]
            else:
                c += 1
                k = i
            chotu[i] = c

        # 1 if chotu[-1] - chotu[i] == 0
        # print(chotu)
        # print()
        sssss = 0
        
        expectd = a[1] - a[0]
        for i in range(2,n):

            if a[i] - a[i-1] <= expectd:
                sssss += 1
                if sssss == 2:
                    break
                kot = i
            else:
                expectd == a[i] - a[i-1]
            diffu[i] = sssss

        # print(diffu)
        # print(a[2] - a[1] < a[1] - a[0])
        loker = [0]*3
        if sssss==1 and n>3 and kot <n-1 and kot > 1 and a[kot+1] - a[kot-1] > a[kot-1] - a[kot-2]:
            if kot == 2:
                loker[0] = 1
            if a[kot+1] - a[kot-1] > a[kot-1] - a[kot-2]:
                loker[2] = 1
            loker[1] = 1
            # print(loker)

            flag = True
        else:
            flag = False
        # print(c)
        if c == 1:
            print("0"*(k),"1","0"*(n-k-1),sep="")
        elif flag:
            print("0"*(kot-2),loker[0],loker[1],loker[2],"0"*(n-kot-1),sep="")
        elif sssss == 1 and n == 3:
            print("1"*3)
        elif sssss or c:
            print("0"*n)
        else:

            print("1"*n)
            
        # expected = a[1] -  a[]
        # for i in range(n):



