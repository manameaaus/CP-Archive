t = int(input())
for i in range(t):
    n , k= map(int,input().split())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    x = [l[0]]
    for i in range(1,n):
        x.append(l[i]+x[i-1])
    
    if k in x:
        print(0)
    else:
        oo = -2
        for i in x:
            if i>k:
                oo = x.index(i)
                break
        else:
            print(k-sum(l))
            
        if oo>-1:
            ppp = []
            for i in range(oo):
                ppp.append(k-x[i])
            print(min(ppp))