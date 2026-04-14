t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    if (a+b) % 3 ==0:
        if min(a,b)>=max(a,b)//2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")