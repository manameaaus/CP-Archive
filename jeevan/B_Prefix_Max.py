t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    temp = l[::]
    maxa = 0
    for i in range(n):
        for j in range(i,n):
            curr = 0
            k_max = 0
            l[i],l[j] = l[j],l[i]
            
            for k in range(n):
                curr = max(curr,l[i])
                k_max += curr

            # if i == 0 and j == 1:
            #     print(curr)
            #     print(l)

            l[i],l[j] = l[j],l[i]
            maxa = max(maxa,k_max)
            

    print(maxa)
