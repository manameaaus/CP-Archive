t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    maxa = -float('inf')
    d = {}
    for i in range(n):
        if a[i]-b[i] in d:
            d[a[i]-b[i]].append(i+1)
        else:
            d[a[i]-b[i]] = [i+1]

        maxa = max(maxa,a[i]-b[i])

    print(len(d[maxa]))
    print(*d[maxa])

    