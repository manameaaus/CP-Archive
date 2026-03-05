t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    l = [i for i in range(n)]
    flag  = True
    for i in range(n):
        if l[i] == x:
            flag = False
        else:
            print(i,end=" ")
    if flag == False:
        print(x)
    else:
        print()
