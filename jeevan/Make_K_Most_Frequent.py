t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    def freq(lis):
        d = {}
        for i in lis:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        return d
    d = freq(a)
    maxa = max(d.values())
    maxb = maxa
    if d[k]==maxa:
        print(0)
    else:
        ans = 2
        b = a[:]
        db = d.copy()
        for i in range(n):
            if d[k] < maxa:
                d[a[i]]-=1
                maxa = max(d.values())
            elif d[k]>=maxa:
                ans = 1
                break
            if d[k]==0:
                break
        if ans == 2:

            for i in range(n-1,-1,-1):
                if db[k] < maxb:
                    db[b[i]]-=1
                    maxb = max(db.values())

                elif db[k]>=maxb:
                    ans = 1
                    break
                if db[k]==0:
                    break
        if ans == 1:
            print(1)
        else:
            print(2)

            




