t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))

    maxa = 0
    max_lis_cost = [0] * n


    for i in range(n):
        max_lis_cost[i] = c[i]
        for j in range(i):
            if a[j] <= a[i]:
                max_lis_cost[i] = max(max_lis_cost[i] , max_lis_cost[j] + c[i])
        maxa = max(maxa,max_lis_cost[i])

    print(sum(c) - maxa)
