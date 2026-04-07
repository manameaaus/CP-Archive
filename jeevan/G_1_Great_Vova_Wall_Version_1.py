n = int(input())
l = [i % 2 for i in list(map(int,input().split()))]
curr = []

for i in range(n):
    if curr and curr[-1] == l[i]:
        curr.pop()
    else:
        curr.append(l[i])

if len(curr) < 2:
    print("YES")
else:
    print("NO")
