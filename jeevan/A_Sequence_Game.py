t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    x = int(input())

    l.sort()

    # if n == 1:
    #     if l[0] == x:

    if l[0] <= x and x <= l[-1]:
        print("YES")
    else:
        print("NO")