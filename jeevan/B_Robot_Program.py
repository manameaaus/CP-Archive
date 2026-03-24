t = int(input())
for i in range(t):
    n,x,k = map(int,input().split())
    s = input()
    flag1 = False
    flag2 = False
    zero,nega = -1,-1
    c = 0
    for i in range(n):
        if s[i] == "L":
            c -= 1
        else:
            c += 1
        if c == -x and nega == -1:
            nega = i+1
            flag2 = True
        if c == 0 and zero == -1:
            zero = i+1
            flag1 = True 
        if flag1 and flag2:
            k -= nega
            ans = k//zero
            print(ans+1)
            break       
    else:
        if flag2:
            print(1)
        else:
            print(0)

    




