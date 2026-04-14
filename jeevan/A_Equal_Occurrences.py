t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))



    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    

    # print(d)

    new = []
    for i in d:
        new.append([d[i],i])

    new.sort(reverse = True)


    curr = 0
    ans = 0

    for i in range(len(new)):
        # curr += new[i][0]
        ans = max(ans,(i+1) * new[i][0])

    print(ans)


    
