t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[-1]
    nega = sum(a[i] for i in range(2*n) if i%2==0)
    pos = sum(a[i] for i in range(2*n-1) if i%2)
    print(ans,end=" ")
    for i in range(0,2*n-2,2):
        print(a[i+1],a[i],end = " ")

    print(ans+nega-pos,a[2*n-2])