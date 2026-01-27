t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    # print(a)
    d = {}
    l = []
    c = 0
    x = a[0]
    for j in range(n):
        if x=="":
            x = a[j]
        if a[j]==x:
            c+=1
            
        else:
            d[a[j-1]] = c
            print(a[j])
            l.append(c)
            c = 1
            x = ""
    d[a[-1]] = c
    l.append(c)
    l.sort()
    # print(l)

    
    print(l)
    if k==0:
        print(len(l))
    elif k == len(l):
        print(1)
    else:
        ans = 0
        for i in l:
            if k-i>=0:
                k-=i
            else:
                ans+=1
        print(ans)