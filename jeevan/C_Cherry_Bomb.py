t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    tar = -1
    for i in range(n):
        if b[i] == -1:
            continue
        else:
            if tar == -1:
                tar  = a[i] + b[i]
            elif tar != a[i] + b[i]:
                ans = 0
                break
    else:
        if tar != -1:
            for i in range(n):
                if a[i] > tar or a[i] + k < tar:
                    ans = 0
                    break
            else:
                ans = 1
        else:
            ans = k-(max(a)-min(a))+1
    print(ans)
