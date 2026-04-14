t = int(input())
for i in range(t):
    x,y,a = map(int,input().split())
    z = (a+0.5) // (x+y)
    rem = (a+0.5) - z*(x+y)

    if rem and rem<=x:
        print("NO")
    else:
        print("YES")