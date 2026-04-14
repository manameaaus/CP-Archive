t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    to_look = n+1
    for i in range(n-1,-1,-1):
        if l[i] != i+1:
            to_look = i+1
            break

    
    prod = 1
    for i in range(k):
        ind , p = map(float,input().split())
        if ind >= to_look:
            prod *= (1-p)

    if to_look == n+1:
        print(1)
    else:
        print(1-prod)


    