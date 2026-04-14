t = int(input())
for i in range(t):
    n,m,l = map(int,input().split())
    a = list(map(int,input().split()))
    ref = a[::]

    for i in range(1,n):
        ref[i] -= a[i-1]

    split = min(m,n+1)
    
    run = [0,0]
    val = [0,0]

    
    did = 1
    for i in range(n):
        # print(ref[i])
        if i!= 0 and split == m:
            # if i == 2:
            #     print(ref[i],"opp")
            if run[0]:
                ref[i] -= val[0]
                run[0] += 1

            else:
                if ref[i] >= val[1]:
                    ref[i] -= val[1]
                    run[1] += 1
                else:
                    val[0] = ref[i]
                    run[0] = 1
                    ref[i] = 0
                # if 

        elif i!= 0 and split != m and run[0] + run[1] > split and did:
            run[0] -= 1
            did = 0

        # if i == 1:
        #     print(ref[i],"lll")
        #     print(val)
        #     print(run)
        #     print(".     &.   && ")
        if ref[i] <= run[0]:
            run[0] -= ref[i]
            run[1] += ref[i]
            run[1] -= 1
            
            if run[1] == 0:
                val[1] = val[0]
                val[0] = 0
        else:
            ref[i] -= run[0]
            run[0] = 0
            val[0] = 0
            

            if ref[i] % split:
                # if i == 1:
                #     print(ref[i],split,'kkk')
                run[1] = ref[i] % split
                run[0] += (split - (ref[i] % split))
                val[0] = val[1] + (ref[i] // split)
                val[1] += (ref[i] // split) + 1
            else:
                run[1] = split
                val[1] += (ref[i] // split)


            # if i == 1:
            #     print(val[1],"::)()",ref[i],split,(ref[i] // split) + (1 - (ref[i] % split != 0)))
            # val[1] += (ref[i] // split) + (1 - (ref[i] % split == 0))

            
            # if i == 1:
            #     print(val[1],"::)()")
            run[1] -= 1
            # if val[0] == 0 and split == m:
            #     run[0] += 1
            if run[1] == 0:
                val[1] = val[0]
                val[0] = 0
                run[1] = run[0]
                run[0] = split-run[1]



        split = min(m,n-i)

        # print(val)
        # print(run)
        # print(split,a[i])
        # print("***")

    print(val[1] + l - a[-1])
