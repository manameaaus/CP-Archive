t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    c = list(map(int,input().split()))
    r = list(map(int,input().split()))
    ss = "sssaa"
    d = {}
    for i in range(n):
        radi = r[i]**2

        for j in range(c[i]-r[i],c[i]+r[i]+1):
            
            base = abs(c[i] - j)**2            
            maxy = (((radi-base)**(0.5))//1)


            if (j,ss) not in d:
                d[(j, ss)] = (2*maxy)+1
            else:
                d[(j,ss)] = max(d[(j,ss)],(2*maxy)+1)

    # print(d)
    print(int(sum(d.values())))

 
