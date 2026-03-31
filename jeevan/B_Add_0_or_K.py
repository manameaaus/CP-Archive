t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))


    for i in range(n):
        l[i] += (l[i] % (k+1)) * k

    print(*l)