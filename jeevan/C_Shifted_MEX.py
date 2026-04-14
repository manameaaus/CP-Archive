t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(set(l))

    if len(l) == 1:
        print(1)
        continue
    
    ddd = [l[i]-l[i-1] for i in range(1,len(l))]
    curr = ddd[0]
    c = 0
    ans = 0
    for i in range(len(ddd)):
        if curr == ddd[i]:
            c += 1
        else:
            if curr == 1:
                ans = max(ans,c)
            c = 1
            curr = ddd[i]

    if curr == 1:
        ans = max(ans,c)
    c = 1
    curr = ddd[i]

    print(ans+1)
    # print(ddd)

    