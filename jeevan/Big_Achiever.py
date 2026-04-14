t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    maxa = a[0]
    print(1,end=" ")
    for i in range(1,n):
        if a[i]>maxa:
            print(1,end=" ")
            maxa = a[i]
        else:
            print(0,end= " ")
    print()