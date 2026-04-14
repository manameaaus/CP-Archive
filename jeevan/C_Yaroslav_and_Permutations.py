n = int(input())
a = list(map(int,input().split()))
curr = a[0]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
maxa = max(d.values())

if n < 2*maxa-1:
    print("NO")
else:
    print("YES")    
