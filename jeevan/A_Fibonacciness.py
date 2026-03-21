t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    if (a[3]-a[2] == a[0]+a[1] and 2*a[2] == a[1]+a[3]):
        ans = 3
    elif ((a[0]+a[1]+a[1]==a[2] and a[0]+a[1]+a[2]==a[3])):
        ans = 3
    elif (a[3]+a[1]==a[2]*2 or a[0]+a[1]+a[1] == a[2]) or (a[0]+a[1]==a[3]-a[2]):
        ans = 2
    else:
        ans = 1
    print(ans)