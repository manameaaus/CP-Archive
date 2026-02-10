def fun(i,curr):
    if a[curr] not in donkey:
        donkey[a[curr]], donkey[b[curr]]  = i, n-1-i
        top[a[curr]] = True
        return True
    else:
        if not top[a[curr]]:
            top[a[curr]] = True
            if i == donkey[a[curr]]:
                return True
            ans.append([i+1,donkey[a[curr]]+1])
            return False
        return True

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    valid = True
    same = 0
    d = {}
    for i in range(n):
        if a[i] == b[i]:
            same += 1
        if a[i] in d:
            if d[a[i]] != b[i]:
                valid = False
        else:
            d[a[i]] = b[i]
            d[b[i]] = a[i]


    if (not valid) or (n%2 and same!=1) or (n%2==0 and same!=0):
        print(-1)
    else:
        ans = []
        if n%2:
            for i in range(n):
                if a[i] == b[i] and i != n//2:
                    ans.append([i+1,n//2+1])
                    a[i],a[n//2] = a[n//2],a[i]
                    b[i],b[n//2] = b[n//2],b[i]
        top = [False] * (n+1)
        donkey = {}
        for i in range(n):
            if top[a[i]] or (n%2 and i == n//2):
                continue
            else:
                extra = i
                while not fun(i,extra):
                    extra = donkey[a[extra]]
        
        print(len(ans))
        for i in ans:
            print(*i)

