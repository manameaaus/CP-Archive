n = int(input())
l = [i for i in list(map(int,input().split()))]
curr = []
maxa = 0

for i in range(n):
    if curr and curr[-1] == l[i] and l[i] >= maxa:
        maxa = max(maxa,l[i])
        curr.pop()
    else:
        if curr:
            if curr[-1] < l[i]:
                print("NO")
                break
            
        curr.append(l[i])
        maxa = 0
else:
    if (len(curr) == 0) or (len(curr) == 1 and curr[0] == max(l)):
        print("YES")
    else:
        print("NO")