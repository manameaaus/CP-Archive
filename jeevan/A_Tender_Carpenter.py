t = int(input())
for i in range(t):
    n = int(input())
    a =list(map(int,input().split()))
    ans = "NO"
    for i in range(n-1):
        if max(a[i],a[i+1])<2*(min(a[i],a[i+1])):
            ans = "YES"
    print(ans)
