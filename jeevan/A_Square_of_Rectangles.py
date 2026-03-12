t = int(input())
for i in range(t):
    l1,b1,l2,b2,l3,b3 = map(int,input().split())
    big = [l1,b1]
    mid = [l2,b2]
    small = [l3,b3]

    if(big[0] > big[1]):
        req = big[0] - big[1]
        if small[1] == req and mid[1] == req:
            if small[0]+mid[0] == big[0]:
                print("YES")
            else:
                print("NO")
        elif small[1]+mid[1] == req:
            if small[0] == mid[0] == big[0]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    elif(big[1] > big[0]):
        req = big[1] - big[0]
        if small[0] == req and mid[0] == req:
            if small[1]+mid[1] == big[1]:
                print("YES")
            else:
                print("NO")
        elif small[0]+mid[0] == req:
            if small[1] == mid[1] == big[1]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        exp = big[0]
        if small[0] == exp and mid[0] == exp:
            if small[1]+mid[1] == big[1]:
                print("YES")
            else:
                print("NO")
        elif small[1] == exp and mid[1] == exp:
            if small[0]+mid[0] == big[0]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")  # code ends here


            