t = int(input())
for i in range(t):
    n,s = map(int,input().split())
    c = 0
    for i in range(n):
        d1,d2,x,y = map(int,input().split())
        if (x == y):
            if (d1==d2==1 or d1==d2==-1):
                c+=1
                
        if (x+y == s):
            if (d1==1 and d2==-1 or d1==-1 and d2==1):
                c+=1

    print(c)

