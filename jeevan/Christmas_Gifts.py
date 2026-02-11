t = int(input())
for i in range(t):
    h,l,w = map(int,input().split())
    ans = 2*(h*l+l*w+w*h)
    print(1000//ans)