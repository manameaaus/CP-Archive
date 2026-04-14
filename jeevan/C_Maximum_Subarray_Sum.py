t = int(input())
for i in range(t):
    n ,k = map(int,input().split())
    s = input()
    l = list(map(int,input().split()))


    curr = 0
    maxa = 0

    zero = -1
    sunya = 0

    for i in range(n):
        if s[i] != "0":
            curr = max(curr+l[i],l[i])
            maxa = max(maxa,curr)
        else:
            curr = 0

    if maxa > k:
        print("No")
        continue
    # if maxa == k:
    #     print("Yes")
    #     print(*l)
    #     continue

    for i in range(n):
        if s[i] == "0":
            zero = i

    if maxa < k and zero == -1:
        print("No")
        continue

    right = 0
    left = 0
    c = 0

    for i in range(zero+1,n):
        if s[i] != "0":
            c += l[i]
            right = max(right,c)
        else:
            break
    
    c = 0
    for i in range(zero-1,-1,-1):
        if s[i] != "0":
            c += l[i]
            left = max(left,c)
        else:
            break

    print("Yes")
    ro = -10**18
    for i in range(n):
        if s[i] != "0":
            print(l[i],end = " ")
        else:
            if i == zero:
                print(k-left-right,end = " ")
            else:
                print(ro,end = " ")
    print()


    
    


        

    # if sunya == 0 and maxa 

    # -10 -20 5 10 15 -31 10 0 2 3 4 5

    # 10 -90 0 -8 20
    # 30
    # 200 250 -250 100 -50 100 -50 150
    # 450
            

