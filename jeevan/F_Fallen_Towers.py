t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    point = 0
    while i<n:
        j = i
        while j+1<n and a[j+1]==a[i]:
            j+=1
        
        v = a[i]
        if i==0 or a[i-1]<v:
            if j==n-1 or a[j+1]<v:
                ans+=1
        point = 2*j + 2
        i = j+1
        pr
    print(ans)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    while i<n:
        j = i
        while j+1<n and a[j+1]==a[i]:
            j+=1
        v=a[i]
        if i==0 or a[i-1]<v:
            if j==n-1 or a[j+1]<v:
                ans+=1
        i = j+1
    print(ans)