t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))


    def solve(n,a,b):
        

        maxa = -1

        for i in range(n):
            if a[i] != b[i]:
                maxa = i


        if maxa == -1:

            aj = a.count(1) % 2
            bj = b.count(1) % 2

            if aj == bj:
                return("Tie")
            elif aj > bj:
                return("Ajisai")
            else:
                return("Mai")
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
                return('Tie')
            else:
                if maxa % 2 == 1:
                    return("Mai")
                else:
                    return("Ajisai")

    for i in range(20,-1,-1):
        tempa = [(j & (1 << i)) for j in a]
        tempb = [(j & (1 << i)) for j in b]
        ans = solve(n,tempa,tempb)
        if ans != "Tie":
            print(ans)
            break
    else:
        print("Tie")





