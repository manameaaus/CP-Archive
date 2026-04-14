t = int(input())
for i in range(t):
    n = int(input())
    if n%2:
        print(n,end = " ")
        for i in range(1,n):
            print(i,end = " ")
        print()
    else:
        print(-1)