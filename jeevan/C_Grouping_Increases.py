t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    uppar = l[0]
    niche = float("inf")

    penalty = 0
    for i in range(1,n):
        if l[i] <= uppar and l[i] <= niche:
            if uppar < niche:
                uppar = l[i]
            else:
                niche = l[i]
        elif l[i] > uppar and l[i] > niche:
            penalty += 1
            if uppar < niche:
                uppar = l[i]
            else:
                niche = l[i]
        else:
            if uppar >= l[i]:
                uppar = l[i]
            else:
                niche = l[i]

    print(penalty)


