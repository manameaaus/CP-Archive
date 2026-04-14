n = int(input())
a = list(map(int,input().split()))
a.sort()
maxa = a[-1] - a[0]
i = 0
j = n-1
if a[0] != a[-1]:
    c = a.count(a[0]) * a.count(a[-1])
else:
    c = int(n*(n-1)/2)
print(maxa,c)


    