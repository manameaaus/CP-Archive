def doit(a):
    x = len(a)
    b = [0]*(x-1)

    for i in range(x-1):
        b[i] = a[i+1]-a[i]
    return b
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxa = sum(a)
    while len(a)>1:
        a = doit(a)
        if sum(a)<0:
            a = a[::-1]
        maxa = max(maxa,abs(sum(a)))
    print(maxa)