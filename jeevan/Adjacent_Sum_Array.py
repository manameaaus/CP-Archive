t = int(input())
for i in range(t):
    n = int(input())
    lis = list(map(int,input().split()))
    lis.sort()
    x = 1
    print(1,end=" ")
    for i in lis:
        print(i-x,end=" ")
        x = i-x
    print()