t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    if l[0]==l[1]==l[2]==l[3]:
        print("YES")
    else:
        print("NO")