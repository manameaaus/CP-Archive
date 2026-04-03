t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    used = set()
    unused = set(range(1,n+1))


    for i in l:
        if i in unused:
            unused.remove(i)
            used.add(i)


    if len(unused) >= 2:
        lis = list(used)
        lis1 = list(unused)

        h = [lis1[0],lis1[1],lis[0]]
        l = []

        for i in range(k):
            l.append(h[i%3])

        print(*l)
    else: 
        if len(unused) == 0:
            hhh  = []
            for i in range(k):
                hhh.append(l[i%n])

            print(*hhh)
        else:

            lis1 = list(unused)
            last = l[-1]
            used.remove(last)
            if len(used) == 0:
                h = [lis1[0],last]
                l = []

                for i in range(k):
                    l.append(h[i%2])   

                print(*l) 
            else:
                lis = list(used)
                
                h = [lis1[0]]
                for i in used:
                    h.append(i)
                    break
                h.append(last)

                l = []

                for i in range(k):
                    l.append(h[i%3])   
                print(*l) 

                