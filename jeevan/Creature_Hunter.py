# cook your dish here
t = int(input())
for i in range(t):
    n,h = map(int,input().split())
    maxa1 = -1
    maxa2 = -1
    # sec = []
    for i in range(n):
        x,y = map(int,input().split())
        if x == 2:
            maxa2 = max(maxa2,y)
            # sec.append(y)
        else:
            maxa1 = max(maxa1,y)
    # sec.sort(reverse = True)      
    if h <= maxa1:
        print(1)
    else:
        if maxa1*2 >= maxa2:
            if h%maxa1 == 0:
                print(h//maxa1)
            else:
                print((h//maxa1) + 1)
        else: 
            key = (2 * (h//maxa2))
            ans = 0
            pot = h%maxa2
            rem = pot
            if pot == 0:
                print(key)
            else:
                if pot <= maxa1:
                    print(key+1)
                else:
                    print(key+2)
                