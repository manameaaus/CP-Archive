t = int(input())
for i in range(t):
    n,x,k = map(int,input().split())
    s = input()
    c = 0
    ko = 0
    l = [0]
    dr = []
    sin = []
    for i in s:
        if i == '1':
            c += 1
            ko+=1
        else:
            l.append(l[-1]+c)
            dr.append(ko)
            sin.append(c)
            ko = 0
    l = l[1:]
    print(l)
    print(dr)
    print(sin)


