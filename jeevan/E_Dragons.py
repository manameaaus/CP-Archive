s,n = map(int,input().split())
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,-y])

l.sort()

for i in l:
    if i[0] < s:
        s -= i[1]
    else:
        print("NO")
        break
else:
    print("YES")
