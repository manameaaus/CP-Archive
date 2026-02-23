t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = 0
    while i<n:
        j=i
        while j+1<n:
            if a[j+1]!=a[i]:
                break
            j+=1

        v=a[i]
        fir = (i==0) or a[i-1]<v
        sec = (j==n-1) or a[j+1]<v
        if fir and sec:
            ans+=1
        i = j+1
    print(ans)