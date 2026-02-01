t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l = []
    for k,v in d.items():
        l.append([v,k])
    l.sort(reverse=True)
    
    
    maxc = l[0][1]
    cx = s.index(maxc)
    minc = l[-1][1]
    cy = s.index(minc)

    for i in range(n):
        if i==cy:
            print(maxc,end="")
        else:
            print(s[i],end="")
    print()
