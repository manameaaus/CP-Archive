t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    maxa = l.index(max(l))

    if l.count(l[-1]) == n:
        print("No")
    else:
        print("Yes")
        for i in range(n):
            if i == maxa:
                print(2,end=" ")
            else:
                print(1,end = " ")
        print()
        