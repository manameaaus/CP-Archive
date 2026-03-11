t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    run = [0] * n
    first = [n+1] * n
    last = [0] * n
    last[0] = 1
    for i in range(1,n):
        if l[i] != l[i-1]:
            run[i] = 1

        run[i] += run[i-1]
        first[run[i]] = min(first[run[i]],i+1)
        last[run[i]] = max(last[run[i]],i+1)

    q = int(input())
    for i in range(q):
        l,r = map(int,input().split())
        l -= 1
        r -= 1
        if run[l] == run[r]:
            print(-1,-1)
        else:
            print(first[run[r]],last[run[r]-1])


