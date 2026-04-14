t = int(input())
for i in range(t):
    n,x,y = map(int,input().split())
    l = [int(i) for i in input()]
    sunm = sum(i//4 for i in l)
    if sunm >= x+y:
        print("YES")
    else:
        print("NO")