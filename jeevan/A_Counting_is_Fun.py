t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 1
    maxa = a[0]
    for i in range(1,n):
        if a[i] == -1:
            c*=a[i+1]-a[i-1]-1
        else:
            if a[i] > maxa:
                maxa = a[i]
            else:
                print(0)
                break
    else:
        print(c%(10**9+7))