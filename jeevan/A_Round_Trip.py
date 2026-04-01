t = int(input())
for i in range(t):
    r,x,d,n = map(int,input().split())
    s = list(input())


    if r >= x:
        minus = -1
        for i in range(n):
            if s[i] == 2:
                minus = i
            else:
                break
        
        c = 0
        for i in range(minus+1,n):
            if r < x:
                c += 1
            else:
                if s[i] == "1":
                    c += 1
                    r -= d
                    r = max(r,0)


        print(c)
    else:
        print(n)