n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
maxa = l[n-1] - l[0]
for i in range(1,m-n+1):
    maxa = min(maxa,l[n-1+i] - l[i])
print(maxa)