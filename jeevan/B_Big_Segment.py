t = int(input())
lis = {}
ris = set()

for i in range(t):
    l,r = map(int,input().split())
    if l in lis:
        lis[l].append([r,i+1])
    else:
        lis[l] = [[r,i+1]]
    ris.add(r)

rmax = max(ris)
lmin = min(lis.keys())

for i in lis[lmin]:
    # print(i)
    if i[0] >= rmax:
        print(i[1])
        break
else:
    print(-1)

    


